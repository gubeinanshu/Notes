
# 读取显示图片
```python

# -*- coding: utf-8 -*-
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while 1:
    # 得到每一帧图像
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    # 转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 卷积核
    kernel = np.ones((3, 3), np.float32) / 25
    # 平滑，降噪
    dst = cv2.filter2D(gray, -1, kernel)
    # Canny 边缘检测
    edges = cv2.Canny(dst, 20, 20)
    # 显示每一帧图像
    cv2.imshow("capture", edges)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    # 延时 30 ms，任意键退出
    # if(cv2.waitKey(30) >= 0):
    #     break

cap.release()
cv2.destroyAllWindows()


```

# 形态学腐蚀
```python

# -*- coding: utf-8 -*-

import cv2
import numpy as np

# Load an color image in grayscale
"""
就像土壤侵蚀一样，这个操作会把前景物体的边界腐蚀掉（但是前景仍然
是白色）。这是怎么做到的呢？卷积核沿着图像滑动，如果与卷积核对应的原图
像的所有像素值都是1，那么中心元素就保持原来的像素值，否则就变为零。
这回产生什么影响呢？根据卷积核的大小靠近前景的所有像素都会被腐蚀
掉（变为0），所以前景物体会变小，整幅图像的白色区域会减少。这对于去除
白噪声很有用，也可以用来断开两个连在一块的物体等。
"""
# 读入图像
img = cv2.imread('t.png', cv2.IMREAD_COLOR)
# 卷积核
kernel = np.ones((5, 5), np.uint8)
# 腐蚀
erosion = cv2.erode(img, kernel, iterations=1)
# 第一个参数是窗口名称， 第二个是要显示的图片
cv2.imshow('image', img)
cv2.imshow('image2', erosion)
# 0 等待任意键按下， >0 时为等待多少毫秒
cv2.waitKey(0)
cv2.destroyAllWindows()


```

# 图像平滑_2D卷积
```python

# -*- coding: utf-8 -*-

import cv2
import numpy as np

"""
将核放在图像的一个像素A 上，求与核对应的图像上25（5x5）
个像素的和，在取平均数，用这个平均数替代像素A 的值。重复以上操作直到
将图像的每一个像素值都更新一边
"""

# 读入图像
img = cv2.imread('t.png', cv2.IMREAD_COLOR)
# 卷积核
kernel = np.ones((5, 5), np.float32)/25
# 平滑
dst = cv2.filter2D(img, -1, kernel)
# 第一个参数是窗口名称， 第二个是要显示的图片
cv2.imshow('image', img)
cv2.imshow('image2', dst)
# 0 等待任意键按下， >0 时为等待多少毫秒
cv2.waitKey(0)
cv2.destroyAllWindows()


```

# 播放视频

"""
要安装 ffmpeg 可参考：[python + opencv: 解决不能读取视频的问题](http://blog.csdn.net/heyijia0327/article/details/44034671)


两种方法都需要完成的共同一步是：
找到opencv安装路径下的\sources\3rdparty\ffmpeg文件夹，如D:\soft setup pack\Python_setpack\opencv\sources\3rdparty\ffmpeg。将文件夹中的opencv_ffmpeg.dll文件名修改为opencv_ffmpeg2410.dll，如果你安装的是opencv2.4.9，那就修改成opencv_ffmpeg249.dll。其他版本依次类推。如果你是64位的系统，那就修改opencv_ffmpeg_64.dll文件名为opencv_ffmpeg2410_64.dll。
1. 方法1：将opencv_ffmpeg2410.dll复制到E:\programming soft\python2.7文件夹下即可，其中E:\programming soft\为python安装路径。
2. 方法2：在windows的环境变量中添加上D:\soft setup pack\Python_setpack\opencv\sources\3rdparty\ffmpeg，其中D:\soft setup pack\Python_setpack\为博主电脑上OpenCv的安装路径。
"""

```python

# -*- coding: utf-8 -*-
import numpy as np
import cv2

cap = cv2.VideoCapture("./t.mp4")

while 1:
    # 得到每一帧图像
    ret, frame = cap.read()
    # 显示每一帧图像
    cv2.imshow("capture", frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


```

# Canny 边缘检测
```python

# -*- coding: utf-8 -*-

import cv2
import numpy as np

"""
将核放在图像的一个像素A 上，求与核对应的图像上25（5x5）
个像素的和，在取平均数，用这个平均数替代像素A 的值。重复以上操作直到
将图像的每一个像素值都更新一边
"""

# 读入原始图像，转换为灰度图像
img = cv2.imread('t2.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 直接以灰度读取
# img = cv2.imread('t.png', cv2.IMREAD_GRAYSCALE)
# 卷积核
kernel = np.ones((3, 3), np.float32)/25
# 平滑，降噪
dst = cv2.filter2D(img, -1, kernel)
# Canny 边缘检测
edges = cv2.Canny(dst, 10, 10)
# 第一个参数是窗口名称， 第二个是要显示的图片
cv2.imshow('image', img)
cv2.imshow('image2', edges)
# 0 等待任意键按下， >0 时为等待多少毫秒
cv2.waitKey(0)
cv2.destroyAllWindows()


```

# 从摄像头获取并处理
```python

# -*- coding: utf-8 -*-
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while 1:
    # 得到每一帧图像
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    # 转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 卷积核
    kernel = np.ones((3, 3), np.float32) / 25
    # 平滑，降噪
    dst = cv2.filter2D(gray, -1, kernel)
    # Canny 边缘检测
    edges = cv2.Canny(dst, 20, 20)
    # 显示每一帧图像
    cv2.imshow("capture", edges)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    # 延时 30 ms，任意键退出
    # if(cv2.waitKey(30) >= 0):
    #     break

cap.release()
cv2.destroyAllWindows()


```

