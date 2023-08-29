from keras.models import load_model
# 모델 다운
model = load_model('4-snack.h5')

import time
import os
from PIL import Image
import sys
import numpy as np
from tensorflow.keras.preprocessing import image
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.applications.inception_resnet_v2 import InceptionResNetV2, preprocess_input

categories = {'cola': 0,
                    'pocachip': 1,
                    'shrimpsnacker': 2,
                    'sprite': 3}


imagefiles = os.listdir(os.getcwd())  # 디렉토리 저장
imagelen = len(os.listdir(os.getcwd())) # 파일 개수
count=0

for path in imagefiles:
    if count>=2:
        img=image.load_img(path, target_size=(150, 150))

        x=image.img_to_array(img)
        x=np.expand_dims(x, axis=0)
        images = np.vstack([x])

        classes = model.predict(images, batch_size=10)

        df = pd.DataFrame({'pred':classes[0]})
        df = df.sort_values(by='pred', ascending=False, na_position='first')

        print("사진 이름 : "+path)

        for x in categories:
            if categories[x] == (df[df == df.iloc[0]].index[0]):
                print("결과 = "+x)
                        
    count=count+1
    if count==32:
        break

