from keras.models import load_model
import time
import os
from PIL import Image
import sys
import numpy as np
from tensorflow.keras.preprocessing import image
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.applications.inception_resnet_v2 import InceptionResNetV2, preprocess_input
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import base64
from io import BytesIO


# 모델 다운
model = load_model('4-snack.h5')
# 카테고리
categories = {'cola': 0,
                'pocachip': 1,
                'shrimpcracker': 2,
                'sprite': 3}

# engine = create_engine('mysql://test:4444@192.168.35.195/image_upload?charset=utf8,', echo=False)
engine = create_engine("mariadb+mariadbconnector://test:4444!@192.168.35.195:3306/image_upload")

sql = "SELECT image_data from images"  # 이미지 가져오기


img_df = pd.read_sql(sql=sql, con=engine) #mysql 에서 데이터 가져와서 읽기
img_str = img_df['image_data'].values[0]
img = base64.b64decode(img_str)
          
im = Image.open(BytesIO(img))
im = im.convert("RGB")
im.save('test.jpg','JPEG') # 저장
path = 'test.jpg'

img=image.load_img(path, target_size=(150, 150))
x=image.img_to_array(img)
x=np.expand_dims(x, axis=0)
images = np.vstack([x])
classes = model.predict(images, batch_size=10)
df = pd.DataFrame({'pred':classes[0]})
df = df.sort_values(by='pred', ascending=False, na_position='first')
for x in categories:
    if categories[x] == (df[df == df.iloc[0]].index[0]):
        print("결과 = "+x)


'''
while 1:
    #image_db=pymysql.connect(user='test', password='4444',
                                 #host='192.168.35.195',db='image_upload',port = 3306, charset='utf8') #DB 연동


    engine = create_engine("mysql+pymysql://test:4444@192.168.35.195:3306/image_upload,", echo=False)

    sql = "SELECT image_data from images"  # 이미지 가져오기
    sql_count = "SELECT COUNT(image_data) from images" # 이미지 개수 확인
    sql_delete = "DELETE from images"      # 이미지 지우기

    
    img_df = pd.read_sql(sql, con=engine) #mysql 에서 데이터 가져와서 읽기
    img_str = img_df['image_data'].values[0]
    img = base64.b64decode(img_str)
          
    im = Image.open(BytesIO(img))
    im = im.convert("RGB")
    im.save('test.jpg','JPEG') # 저장
    path = 'test.jpg'

    img=image.load_img(path, target_size=(150, 150))
    x=image.img_to_array(img)
    x=np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)
    df = pd.DataFrame({'pred':classes[0]})
    df = df.sort_values(by='pred', ascending=False, na_position='first')
    for x in categories:
        if categories[x] == (df[df == df.iloc[0]].index[0]):
            print("결과 = "+x)
              
    image_db.commit()
    image_db.close()
'''
