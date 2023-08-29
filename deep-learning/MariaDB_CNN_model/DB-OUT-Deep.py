import warnings
warnings.filterwarnings("ignore") #경고 안뜨겡

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
import base64
from io import BytesIO
import pymysql


# 모델 다운
model = load_model('4-snack.h5')
# 카테고리
categories = {'콜라 (캔 음료)': 0,
                '포카칩 (봉지 과자)': 1,
                '새우깡 (봉지 과자)': 2,
                '스프라이트 (캔 음료)': 3}


image_db=pymysql.connect(user='pi-t', password='4444',
                         host='localhost''',db='image_upload',port = 3306, charset='utf8') #DB 연동
cur = image_db.cursor()
sql_count = "SELECT COUNT(image_data) from images" # 이미지 개수 확인

cur.execute(sql_count)
result=cur.fetchone()
for count in result:
    count_upload = count + 1
    count_data = count
    print(count_upload)
    print(count_data)
image_db.commit()
image_db.close()


while 1:
    image_db=pymysql.connect(user='pi-t', password='4444',
                                 host='localhost''',db='image_upload',port = 3306, charset='utf8') #DB 연동
    
    cur = image_db.cursor()

    sql = "SELECT image_data from images"  # 이미지 가져오기
    sql_count = "SELECT COUNT(image_data) from images" # 이미지 개수 확인
    sql_delete = "DELETE from images"      # 이미지 지우기

    #sql_print="INSERT INTO print(print_data) VALUES(%s)"

    cur.execute(sql_count) # 데이터 개수 세기
    result = cur.fetchone()
    for data in result:     
        if data == count_upload:
            count_upload=count_upload+1
            img_df = pd.read_sql_query(sql, image_db) #mysql 에서 데이터 가져와서 읽기
            img_str = img_df['image_data'].values[count_data]
            img = base64.b64decode(img_str)
            count_data=count_data + 1
            
            im = Image.open(BytesIO(img))
            im = im.convert("RGB")
            im.save(str(data)+'img.jpg','JPEG') # 저장
            path = (str(data)+'img.jpg')

            img=image.load_img(path, target_size=(150, 150))
            x=image.img_to_array(img)
            x=np.expand_dims(x, axis=0)
            images = np.vstack([x])
            classes = model.predict(images, batch_size=10)
            df = pd.DataFrame({'pred':classes[0]})
            df = df.sort_values(by='pred', ascending=False, na_position='first')
            for x in categories:
                if categories[x] == (df[df == df.iloc[0]].index[0]):
                    print("식품 이름 = "+x)
                    #cur.execute(sql_print, x)

            #cur.execute(sql_delete)
    image_db.commit()
    image_db.close()
