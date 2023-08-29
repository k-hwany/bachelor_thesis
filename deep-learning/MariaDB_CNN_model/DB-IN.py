import pymysql
from PIL import Image
import base64
from io import BytesIO
import time

image_db=pymysql.connect(user='root', password='1234',
                         host='localhost',db='image_upload',charset='utf8') #DB 연동
cur = image_db.cursor()

with open("t-sh3.jpg", "rb") as image_file:
    binary_image = image_file.read()

binary_image = base64.b64encode(binary_image)
binary_image=binary_image.decode('UTF-8')

sql = "INSERT INTO images (image_data) VALUES(%s)"

cur.execute(sql, (binary_image))



image_db.commit()
image_db.close()

print("저장 후 종료")
