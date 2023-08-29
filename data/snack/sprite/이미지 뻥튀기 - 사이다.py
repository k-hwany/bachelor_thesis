import time
import os
from PIL import Image
import sys


x="sprite"
ro = [20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360]




imagefiles = os.listdir(os.getcwd())  # 디렉토리 저장
imagelen = len(os.listdir(os.getcwd())) # 파일 개수

print(imagefiles)
print(imagelen)
count=0
for y in imagefiles: #이미지 하나씩
    image = Image.open(y)
    image = image.convert("RGB")
    image2 = image.transpose(Image.FLIP_LEFT_RIGHT)  # 좌우 대칭
    if count <=30:
        for r in ro:   # 각도
            save=image.rotate(r)
            save.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+y+str(r)+'1.jpg', 'JPEG')  # 원본 돌려 저장
            save2 = image2.rotate(r)  # 좌우대칭 돌리기
            save2.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+y+str(r)+'111.jpg', 'JPEG')
    else:
        for r in ro:   # 각도
            save=image.rotate(r)
            save.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+y+str(r)+'1.jpg', 'JPEG')  # 원본 돌려 저장
            save2 = image2.rotate(r)  # 좌우대칭 돌리기
            save2.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+y+str(r)+'111.jpg', 'JPEG')
    count = count+1
    if count == imagelen-1:
        break

'''
    for i in range(0, imagelen-2):
        
        image = Image.open(imagefiles[i])
        image = image.convert("RGB")
        image2 = image.transpose(Image.FLIP_LEFT_RIGHT)  # 좌우 대칭
    
        if i<=50:
            save1 = image.rotate(20)  # 원본 돌리기
            save2 = image.rotate(40)
            save3 = image.rotate(60)
            save4 = image.rotate(80)
            save5 = image.rotate(100)
            save6 = image.rotate(120)
            save7 = image.rotate(140)
            save8 = image.rotate(160)
            save9 = image.rotate(180)
            save10 = image.rotate(200)
            save11 = image.rotate(220)
            save12 = image.rotate(240)
            save13 = image.rotate(260)
            save14 = image.rotate(280)
            save15 = image.rotate(300)
            save16 = image.rotate(320)
            save17 = image.rotate(340)
            save18 = image.rotate(360)

            save1.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'1.jpg', 'JPEG')  # 원본 돌려 저장
            save2.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'2.jpg', 'JPEG')  # 원본 돌려 저장
            save3.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'3.jpg', 'JPEG')  # 원본 돌려 저장
            save4.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'4.jpg', 'JPEG')  # 원본 돌려 저장
            save5.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'5.jpg', 'JPEG')  # 원본 돌려 저장
            save6.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'6.jpg', 'JPEG')  # 원본 돌려 저장
            save7.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'7.jpg', 'JPEG')  # 원본 돌려 저장
            save8.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'8.jpg', 'JPEG')  # 원본 돌려 저장
            save9.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'9.jpg', 'JPEG')  # 원본 돌려 저장
            save10.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'10.jpg', 'JPEG')  # 원본 돌려 저장
            save11.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'11.jpg', 'JPEG')  # 원본 돌려 저장
            save12.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'12.jpg', 'JPEG')  # 원본 돌려 저장
            save13.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'13.jpg', 'JPEG')  # 원본 돌려 저장
            save14.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'14.jpg', 'JPEG')  # 원본 돌려 저장
            save15.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'15.jpg', 'JPEG')  # 원본 돌려 저장
            save16.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'16.jpg', 'JPEG')  # 원본 돌려 저장
            save17.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'17.jpg', 'JPEG')  # 원본 돌려 저장
            save18.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'18.jpg', 'JPEG')  # 원본 돌려 저장
        
        

            ssave1 = image2.rotate(20)  # 좌우대칭 돌리기
            ssave2 = image2.rotate(40)
            ssave3 = image2.rotate(60)
            ssave4 = image2.rotate(80)
            ssave5 = image2.rotate(100)
            ssave6 = image2.rotate(120)
            ssave7 = image2.rotate(140)
            ssave8 = image2.rotate(160)
            ssave9 = image2.rotate(180)
            ssave10 = image2.rotate(200)
            ssave11 = image2.rotate(220)
            ssave12 = image2.rotate(240)
            ssave13 = image2.rotate(260)
            ssave14 = image2.rotate(280)
            ssave15 = image2.rotate(300)
            ssave16 = image2.rotate(320)
            ssave17 = image2.rotate(340)
            ssave18 = image2.rotate(360)

            ssave1.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'111.jpg', 'JPEG')  
            ssave2.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'222.jpg', 'JPEG')  
            ssave3.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'333.jpg', 'JPEG')  
            ssave4.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'444.jpg', 'JPEG')  
            ssave5.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'555.jpg', 'JPEG')  
            ssave6.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'666.jpg', 'JPEG')  
            ssave7.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'777.jpg', 'JPEG')  
            ssave8.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'888.jpg', 'JPEG')  
            ssave9.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'999.jpg', 'JPEG')  
            ssave10.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'1000.jpg', 'JPEG')  
            ssave11.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'1111.jpg', 'JPEG')  
            ssave12.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'1222.jpg', 'JPEG')  
            ssave13.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'1333.jpg', 'JPEG')  
            ssave14.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'1444.jpg', 'JPEG')  
            ssave15.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'1555.jpg', 'JPEG')  
            ssave16.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'1666.jpg', 'JPEG')  
            ssave17.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'1777.jpg', 'JPEG')  
            ssave18.save('C:/Users/dkslf/.2kkh/data/snack-data/train/train-'+x+'/'+imagefiles[i]+'1888.jpg', 'JPEG')
        else:
            save1 = image.rotate(20)  # 원본 돌리기
            save2 = image.rotate(40)
            save3 = image.rotate(60)
            save4 = image.rotate(80)
            save5 = image.rotate(100)
            save6 = image.rotate(120)
            save7 = image.rotate(140)
            save8 = image.rotate(160)
            save9 = image.rotate(180)
            save10 = image.rotate(200)
            save11 = image.rotate(220)
            save12 = image.rotate(240)
            save13 = image.rotate(260)
            save14 = image.rotate(280)
            save15 = image.rotate(300)
            save16 = image.rotate(320)
            save17 = image.rotate(340)
            save18 = image.rotate(360)

            save1.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'1.jpg', 'JPEG')  # 원본 돌려 저장
            save2.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'2.jpg', 'JPEG')  # 원본 돌려 저장
            save3.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'3.jpg', 'JPEG')  # 원본 돌려 저장
            save4.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'4.jpg', 'JPEG')  # 원본 돌려 저장
            save5.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'5.jpg', 'JPEG')  # 원본 돌려 저장
            save6.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'6.jpg', 'JPEG')  # 원본 돌려 저장
            save7.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'7.jpg', 'JPEG')  # 원본 돌려 저장
            save8.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'8.jpg', 'JPEG')  # 원본 돌려 저장
            save9.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'9.jpg', 'JPEG')  # 원본 돌려 저장
            save10.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'10.jpg', 'JPEG')  # 원본 돌려 저장
            save11.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'11.jpg', 'JPEG')  # 원본 돌려 저장
            save12.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'12.jpg', 'JPEG')  # 원본 돌려 저장
            save13.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'13.jpg', 'JPEG')  # 원본 돌려 저장
            save14.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'14.jpg', 'JPEG')  # 원본 돌려 저장
            save15.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'15.jpg', 'JPEG')  # 원본 돌려 저장
            save16.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'16.jpg', 'JPEG')  # 원본 돌려 저장
            save17.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'17.jpg', 'JPEG')  # 원본 돌려 저장
            save18.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'18.jpg', 'JPEG')  # 원본 돌려 저장
        
        

            ssave1 = image2.rotate(20)  # 좌우대칭 돌리기
            ssave2 = image2.rotate(40)
            ssave3 = image2.rotate(60)
            ssave4 = image2.rotate(80)
            ssave5 = image2.rotate(100)
            ssave6 = image2.rotate(120)
            ssave7 = image2.rotate(140)
            ssave8 = image2.rotate(160)
            ssave9 = image2.rotate(180)
            ssave10 = image2.rotate(200)
            ssave11 = image2.rotate(220)
            ssave12 = image2.rotate(240)
            ssave13 = image2.rotate(260)
            ssave14 = image2.rotate(280)
            ssave15 = image2.rotate(300)
            ssave16 = image2.rotate(320)
            ssave17 = image2.rotate(340)
            ssave18 = image2.rotate(360)

            ssave1.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'111.jpg', 'JPEG')  
            ssave2.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'222.jpg', 'JPEG')  
            ssave3.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'333.jpg', 'JPEG')  
            ssave4.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'444.jpg', 'JPEG')  
            ssave5.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'555.jpg', 'JPEG')  
            ssave6.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'666.jpg', 'JPEG')  
            ssave7.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'777.jpg', 'JPEG')  
            ssave8.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'888.jpg', 'JPEG')  
            ssave9.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'999.jpg', 'JPEG')  
            ssave10.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'1000.jpg', 'JPEG')  
            ssave11.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'1111.jpg', 'JPEG')  
            ssave12.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'1222.jpg', 'JPEG')  
            ssave13.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'1333.jpg', 'JPEG')  
            ssave14.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'1444.jpg', 'JPEG')  
            ssave15.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'1555.jpg', 'JPEG')  
            ssave16.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'1666.jpg', 'JPEG')  
            ssave17.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'1777.jpg', 'JPEG')  
            ssave18.save('C:/Users/dkslf/.2kkh/data/snack-data/validation/validation-'+x+'/'+imagefiles[i]+'1888.jpg', 'JPEG')

print("복사 끝")
'''
