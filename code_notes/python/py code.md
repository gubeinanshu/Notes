
获取当前目录的jpg图片
```python
# -*- coding: utf-8 -*-

import os


def get_imlist(path):
    """
    返回目录中所有 jpg 图像的文件名列表
    :param path:
    :return:
    """
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


# 当前目录下的 jpg 文件
print get_imlist("/")

```


python文件复制移动shutil模块
```python
import shutil

# 从源src复制到dst中去。当然前提是目标地址是具备可写权限。抛出的异常信息为IOException. 如果当前的dst已存在的话就会被覆盖掉
shutil.copyfile( src, dst) 
# 移动文件或重命名
shutil.move( src, dst)  
# 只是会复制其权限其他的东西是不会被复制的
shutil.copymode( src, dst) 
# 复制权限、最后访问时间、最后修改时间
shutil.copystat( src, dst) 
# 复制一个文件到一个文件或一个目录
shutil.copy( src, dst)  
# 在copy上的基础上再复制文件最后访问时间与修改时间也复制过来了，类似于cp –p的东西
shutil.copy2( src, dst)  
# 如果两个位置的文件系统是一样的话相当于是rename操作，只是改名；如果是不在相同的文件系统的话就是做move操作
shutil.copy2( src, dst)  
# 把olddir拷贝一份newdir，如果第3个参数是True，则复制目录时将保持文件夹下的符号连接，如果第3个参数是False，则将在复制的目录下生成物理副本来替代符号连接
shutil.copytree( olddir, newdir, True/Flase)
# 递归删除一个目录以及目录内的所有内容
shutil.rmtree( src ) 
```



Python判断字符串是否为字母或者数字
```python
# 严格解析：有除了数字或者字母外的符号（空格，分号,etc.）都会False
isalnum()  # 判断是否数字和字母的组合
isalpha()  # 判断是否字母，不区分大小写
isdigit()  # 函数判断是否数字
```

zip和izip，同时迭代多个iterable对象
```python
from itertools import izip

# “跟zip()相似，但是返回一个iterator而非list”
with open("a.txt") as fa, open("b.txt") as fb:
	for a,b in izip(fa, fb):
		do_something_with(a, b)
```


win下弹出提示窗
```python
# coding: utf8
import ctypes
ctypes.windll.user32.MessageBoxA(
    0, 
    u"点击确定 开始处理data目录下面的xls文件,分析处理完成后会有提示.^_ ^".encode('gb2312'), 
    u' 信息'.encode('gb2312'), 
    0
)
```


python字典按照value进行排序

```python
sorted(d.items(),key = lambda x:x[1],reverse = True)
```

统计，排序
```python
# coding:utf8
import requests

address = "https://gohttp.nie.netease.com/users/hzsunshx/example.txt"
res = requests.get(address)
res.encoding = 'utf-8'
text = res.text

analysis = {}
word_list = text.replace(".", "").replace(",", "").lower().split(" ")

for word in word_list:
    if word not in analysis:
        analysis[word] = 1
    else:
        analysis[word] += 1

sorted_word_list = sorted(analysis.items(), key=lambda x: (x[1], x[0]), reverse=True)
for i in range(10):
    print sorted_word_list[i][1], sorted_word_list[i][0]
```


python程序退出的两种方法

```python
"""
执行该语句会直接退出程序
该方法中包含一个参数status，默认为0，表示正常退出，也可以为1，表示异常退出
该方法引发的是一个SystemExit异常(这是唯一一个不会被认为是错误的异常)，
当没有设置捕获这个异常将会直接退出程序执行，也可以捕获这个异常进行一些其他操作
"""

import sys
sys.exit()
sys.exit(0)
sys.exit(1)

"""
效果也是直接退出，不会抛出异常，但是其使用会受到平台的限制，
但我们常用的Win32平台和基于UNIX的平台不会有所影响。
"""

os._exit()

"""
抛出 SystemExit 异常. 一般在交互式 Shell 中退出时使用.
"""
exit()
quit()
```

获取文件所在目录或者某个路径的父级目录

```python
from os import path 
#返回当前文件所在的目录 
d = path.dirname(__file__)
parent_path = os.path.dirname(d)
parent_path  = os.path.dirname(parent_path)

#返回d所在目录规范的绝对路径
abspath = path.abspath(d)
```

模拟表单提交

```
"""
python模拟表单提交Multipart/form-data
"""
import json

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

url = "https://arch.s3.netease.com/hzdev-appci/monkeytest/video/local_task/local_device"
# data = {
#     "token": "n7910ljw1234"
# }
headers = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0',
    # 'Referer': url
}
multipart_encoder = MultipartEncoder(
    fields={
        "token": "n7910ljw1234",
        'file': ("video.mp4", open("video.mp4", 'rb'), 'application/octet-stream')
    },
)
headers['Content-Type'] = multipart_encoder.content_type
r = requests.post(url, data=multipart_encoder, headers=headers)
print(r.text)

# r = requests.post(url, data=data, files={"file": open("video.mp4", "rb")}, )
# print(r)
# print(r.json())
```


```python
if sys.version_info >= (3, 0):
    raise RuntimeError("Sorry, requires Python 2.x, not Python 3.x\n")
```

```python
def U(x):
    """Convert to unicode, Python 2.7 use only."""
    return x.decode('utf-8', 'ignore') if type(x) is str else x
```

```python
def safe_connect(addr='127.0.0.1:18812', timeout=60, tick_hook=None):
    """connect with retry."""
    t = Timeout(timeout, "RPYC wait open")
    while t.ticking:
        oldtimeout = socket.getdefaulttimeout()
        try:
            socket.setdefaulttimeout(5)
            conn = connect(addr)
            print("[neco] rpyc connected")
            return conn
        except (socket.error, EOFError):
        # 用于回调判断
            if callable(tick_hook):
                tick_hook()
        finally:
            socket.setdefaulttimeout(oldtimeout)
```

```python
@property
解释：
https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386820062641f3bcc60a4b164f8d91df476445697b9e000
```

```python
内置异常
RuntimeError
ValueError
```

使用断言
```python
assert isinstance(before, numbers.Real)
```