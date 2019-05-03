## ubuntu开启远程ssh登陆本机功能

1. sudo apt-get install openssh-server
2. sudo /etc/init.d/ssh start  将其开启。输入 ps -e | grep ssh 查看是否启动成功了。
3. ssh zhaocx1@127.0.0.1


## 压缩、解压缩
```bash

# 压缩
tar -czvf ***.tar.gz
tar -cjvf ***.tar.bz2
# 解压缩
tar -xzvf ***.tar.gz
tar -xjvf ***.tar.bz2

```
参数说明：

-c  ：创建压缩档案的参数(create；
-x  ：解压缩参数
-t  ：查看压缩包内容

***特别注意，在参数的下达中， c/x/t 仅能存在一个，不可同时存在***

-z  ：是否需要用 gzip 压缩(是否同时具有 gzip 的属性)
-j  ：是否需要用 bzip2 压缩(是否同时具有 bzip2 的属性？)
-v  ：压缩的过程中显示信息
-f  ：要使用的压缩包的名称，注意在 f 之后要立即接档名，不要再加参数


## linux在命令符界面浏览网页

w3m 安装使用：

1. sudo apt-get install w3m
2. w3m www.baidu.com


## Shell中自动输入命令需要接受的键盘输入
1. 有些命令带有命令行参数，可以去掉这种询问（如 debian 软件包管理命令 aptitude）
2. 管道完成。一个毫无意义的例子：echo y | apt install vim（本人最常用）
3. 有些命令绕开标准输入，直接从终端读取应答数据，这种情况可以用 expect 来解决。

## Ubuntu Server切换语言

如果在安装时选择了中文安装，在操作时经常会显示乱码，如果需要设置回英文，则修改 /etc/default/locale，将
LANG="cn_ZH.UTF-8"
LANGUAGE="cn_ZH:cn"
修改成
LANG=”en_US.UTF-8”
LANGUAGE=”en_US:en”
运行 locale 以及 sudo locale-gen en_US.UTF-8，重启即可切换到英文

