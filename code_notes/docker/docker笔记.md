参考： [官方中文](https://docs.docker-cn.com/)
[link](https://www.runoob.com/docker/docker-command-manual.html)
[link](https://blog.csdn.net/itguangit/article/details/80222387)
[link](https://www.cnblogs.com/codelove/p/10056866.html)
[link](https://blog.csdn.net/zmx729618/article/details/72930474/)

[link](https://www.jianshu.com/p/1aa13e55c778?utm_campaign=maleskine&utm_content=note&utm_medium=reader_share&utm_source=weibo)

[link](https://blog.csdn.net/pushiqiang/article/details/78682323)

[link](https://blog.51cto.com/9291927/2310444)

[link](https://www.cnblogs.com/youclk/p/8453526.html)

https://docs.docker-cn.com/get-started/part3/#%E4%BA%86%E8%A7%A3%E6%9C%8D%E5%8A%A1

docker 容器应该被视为一个进程，这个是理解和定义docker的一条基本原则；别把docker看成一个虚拟机；


安装

> 内核需要3.10+

uname -r
uname -a

wget -qO- https://get.docker.com/ | sh

当要以非root用户可以直接运行docker时，需要执行 sudo usermod -aG docker runoob 命令，然后重新登陆，否则会有如下报错

sudo usermod -aG docker usernaem


启动docker后台服务

sudo service docker start

测试运行hello-world

docker run hello-world


镜像加速

鉴于国内网络问题，后续拉取 Docker 镜像十分缓慢，我们可以需要配置加速器来解决，这里使用的是网易的镜像地址：http://hub-mirror.c.163.com。

新版的 Docker 使用 /etc/docker/daemon.json（Linux） 或者 %programdata%\docker\config\daemon.json（Windows） 来配置 Daemon。

请在该配置文件中加入（没有该文件的话，请先建一个）：

{
  "registry-mirrors": ["http://hub-mirror.c.163.com"]
}




使用 docker run 命令来在容器内运行一个应用程序。

输出Hello world

docker run ubuntu:15.10 /bin/echo "Hello world"

运行交互式的容器

docker run -i -t ubuntu:15.10 /bin/bash

-t:在新容器内指定一个伪终端或终端。

-i:允许你对容器内的标准输入 (STDIN) 进行交互。


启动容器（后台模式）

docker run -d ubuntu:15.10 /bin/sh -c "while true; do echo hello world; sleep 1; done"


确认容器有在运行，可以通过 docker ps 来查看
docker ps

CONTAINER ID:容器ID

NAMES:自动分配的容器名称

在容器内使用docker logs命令，查看容器内的标准输出

docker logs 2b1b7a428627

停止容器

docker stop 容器ID
docker stop 容器name

运行一个web应用


docker pull training/webapp  # 载入镜像
docker run -d -P training/webapp python app.py

-d:让容器在后台运行。

-P:将容器内部使用的网络端口映射到我们使用的主机上。

我们也可以通过 -p 参数来设置不一样的端口：
docker run -d -p 5000:5000 training/webapp python app.py

网络端口的快捷方式
docker port bf08b7f2cd89
docker port wizardly_chandrasekhar

查看 WEB 应用程序日志
docker logs [ID或者名字] 可以查看容器内部的标准输出
docker logs -f bf08b7f2cd89
-f: 让 docker logs 像使用 tail -f 一样来输出容器内部的标准输出。

查看WEB应用程序容器的进程
docker top wizardly_chandrasekhar

检查 WEB 应用程序
使用 docker inspect 来查看 Docker 的底层信息。它会返回一个 JSON 文件记录着 Docker 容器的配置和状态信息。

重启WEB应用容器
docker start wizardly_chandrasekhar


docker ps -l 查询最后一次创建的容器：
docker ps -l 

移除WEB应用容器
docker rm wizardly_chandrasekhar  





列出镜像列表
docker images  
REPOSITORY：表示镜像的仓库源

TAG：镜像的标签

IMAGE ID：镜像ID

CREATED：镜像创建时间

SIZE：镜像大小


获取一个新的镜像

docker pull ubuntu:13.10

查找镜像Docker Hub 网址为： https://hub.docker.com/

docker search httpd

NAME:镜像仓库源的名称

DESCRIPTION:镜像的描述

OFFICIAL:是否docker官方发布



docker pull httpd 拖取镜像
docker run httpd 使用这个镜像

更新镜像
可以通过命令 docker commit来提交容器副本
docker commit -m="has update" -a="runoob" e218edb10161 runoob/ubuntu:v2

-m:提交的描述信息

-a:指定镜像作者

e218edb10161：容器ID

runoob/ubuntu:v2:指定要创建的目标镜像名



构建镜像



设置镜像标签
docker tag 860c279d2fec runoob/centos:dev





docker ps -a 查看已经创建的容器

docker ps -s 查看已经启动的容器

docker start con_name 启动容器名为con_name的容器

docker stop con_name 停止容器名为con_name的容器

docker rm con_name 删除容器名为con_name的容器

docker rename old_name new_name 重命名一个容器

























