
```
import os
os.remove(path)  # path是文件的路径，如果这个路径是一个文件夹，则会抛出OSError的错误，这时需用用rmdir()来删除
os.rmdir(path)  # path是文件夹路径，注意文件夹需要时空的才能被删除
os.unlink('F:\新建文本文档.txt')  # unlink的功能和remove一样是删除一个文件，但是删除一个删除一个正在使用的文件会报错。
```


```
import os
path = 'F:/新建文本文档.txt'  # 文件路径
if os.path.exists(path):  # 如果文件存在
    # 删除文件，可使用以下两种方法。
    os.remove(path)  
    #os.unlink(path)
else:
    print('no such file:%s'%my_file)  # 则返回文件不存在
```


```
import os
os.removedirs(path)  # 递归地删除目录。如果子目录成功被删除，则将会成功删除父目录，子目录没成功删除，将抛异常。
```


```
import shutil
shutil.rmtree()
```




