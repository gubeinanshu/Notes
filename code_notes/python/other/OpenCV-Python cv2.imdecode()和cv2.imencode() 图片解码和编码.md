* cv2.imdecode()函数从指定的内存缓存中读取数据，并把数据转换(解码)成图像格式;主要用于从网络传输数据中恢复出图像。
* cv2.imencode()函数是将图片格式转换(编码)成流数据，赋值到内存缓存中;主要用于图像数据格式的压缩，方便网络传输

**imdecode()使用**

```python
# 从网络读取图像数据并转换成图片格式

# -*- coding: utf-8 -*-
import numpy as np
import urllib
import cv2
 
url = 'http://www.pyimagesearch.com/wp-content/uploads/2015/01/google_logo.png'
resp = urllib.urlopen(url)
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)
cv2.imshow('URL2Image',image)
cv2.waitKey()


```

**imencode()使用**
```python
# 将图片编码到缓存，并保存到本地
# -*- coding: utf-8 -*-
import numpy as np
import urllib
import cv2
 
img = cv2.imread('0122.jpg')
# '.jpg'表示把当前图片img按照jpg格式编码，按照不同格式编码的结果不一样
img_encode = cv2.imencode('.jpg', img)[1]
# imgg = cv2.imencode('.png', img)
 
data_encode = np.array(img_encode)
str_encode = data_encode.tostring()
 
# 缓存数据保存到本地
with open('img_encode.txt', 'w') as f:
    f.write(str_encode)
    f.flush

```

**imencode()+imdecode()使用**
```
# 图片编码保存到本地，读取本地文件解码恢复成图片格式
# -*- coding: utf-8 -*-
import numpy as np
import urllib
import cv2
 
img = cv2.imread('0122.jpg')
# '.jpg'表示把当前图片img按照jpg格式编码，按照不同格式编码的结果不一样
img_encode = cv2.imencode('.jpg', img)[1]
# imgg = cv2.imencode('.png', img)
 
data_encode = np.array(img_encode)
str_encode = data_encode.tostring()
 
# 缓存数据保存到本地，以txt格式保存
with open('img_encode.txt', 'w') as f:
    f.write(str_encode)
    f.flush
 
with open('img_encode.txt', 'r') as f:
    str_encode = f.read()
 
nparr = np.fromstring(str_encode, np.uint8)
img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
cv2.imshow("img_decode", img_decode)
cv2.waitKey()
```

或者

```python
# -*- coding: utf-8 -*-
import numpy as np
import urllib
import cv2
 
img = cv2.imread('0122.jpg')
# '.jpg'表示把当前图片img按照jpg格式编码，按照不同格式编码的结果不一样
img_encode = cv2.imencode('.jpg', img)[1]
# imgg = cv2.imencode('.png', img)
 
data_encode = np.array(img_encode)
str_encode = data_encode.tostring()
 
# 缓存数据保存到本地，以txt格式保存
with open('img_encode.txt', 'w') as f:
    f.write(str_encode)
    f.flush
 
with open('img_encode.txt', 'r') as f:
    str_encode = f.read()
 
image = np.asarray(bytearray(str_encode), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)
cv2.imshow('img_decode',image)
cv2.waitKey()
```
