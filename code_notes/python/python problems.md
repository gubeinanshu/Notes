## pip 安装特定版本的 Python 包

```python
pip install -v pycrypto==2.3
```

## pyinstaller将py文件打包为exe

[www.pyinstaller.org](www.pyinstaller.org)
安装方法：pip install pyinstaller 若有依赖，安装即可
```
pyinstaller -F -w -i manage.ico t.py

# -F：打包为单文件
# -w：Windows程序，不显示命令行窗口
# -i：是程序图标，
# t.py 要打包的py文件
```

## python 启动 http 服务

python2：
python -m SimpleHTTPServer 8080

python3：
python -m http.server 80

访问： http://localhost:端口号/路径 （默认路径下打开下 index.xml）

## python输出爱心

```python
print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
```

 对于上面这段语句的解释: [点击这里](https://www.cnblogs.com/vhills/p/8449123.html)

## py2 to py3

参考自：[ 使用python3自带工具2to3.py 转换 python2.x 代码 到python3](http://blog.csdn.net/u012211419/article/details/51136232)

在 python3 安装目录下 Python3\Tools\scripts 有个文件 2to3.py 可以实现转换

本人已将该目录添加到 path 目录，在该目录下有个 2to3.exe 故可以直接执行  
2to3.exe --help      查看帮助信息  
2to3.exe -w 目录     批量转换  
2to3.exe -w 文件     单个转换  

1. 不加-w参数，则默认只是把转换过程所对应的diff内容打印输出到当前窗口而已。
2. 加了"-w"，就是把改动内容，写回到原先的文件了。
3. 加上"-n"，不生成bak文件。
4. 加上"--no-diffs",不显示那一堆输出的内容。

## 函数取别名

> ls = os.linesep 为函数取别名，可提高性能


## python 使用豆瓣的pypi源

> 在国内的强烈推荐豆瓣的源 http://pypi.douban.com/simple/ 注意后面要有/simple目录。 使用镜像源很简单，用-i指定就行了：   
sudo easy_install -i http://pypi.douban.com/simple/ saltTesting   
sudo pip install -i http://pypi.douban.com/simple/ saltTesting



## requirements.txt

使用
```
pip freeze > requirements.txt
```

在另一个环境下使用
```
pip install -r requirements.txt
```