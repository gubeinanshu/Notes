参考：  
https://blog.csdn.net/zmx729618/article/details/72930474/  
https://blog.csdn.net/itguangit/article/details/80246071

--------------------

镜像操作

> Docker把应用程序及其依赖打包在一个image文件里面,可以理解为一个容器的说明书. 通过这个image文件可以生成容器的实例.同一个image文件可以生成同时运行的多个实例.

> image文件是一个二进制文件,实际上,一个image文件往往继承自另外一个image文件,加上一些个性化设置而成.举例来说:你可以在ubuntu的image基础上加上Apache服务器,形成你自己的image.
kj

```
# 查找image
sudo docker search ubuntu
# 说明 查找镜像Docker Hub 网址为： https://hub.docker.com/
NAME:镜像仓库源的名称
DESCRIPTION:镜像的描述
OFFICIAL:是否docker官方发布

# 获取镜像
docker pull ubuntu # 这里是官方镜像
docker image pull library/hello-world
# 官方提供的文件都放在library组里面,所以他是默认组,可以省略
docker image pull hello-world

# 查看当前镜像列表
sudo docker images
docker image ls
# 说明
REPOSITORY：表示镜像的仓库源
TAG：镜像的标签
IMAGE ID：镜像ID
CREATED：镜像创建时间
SIZE：镜像大小

# 删除镜像
docker image rm [imageName]

# 更新镜像，可以通过命令 docker commit来提交容器副本
docker commit -m="has update" -a="runoob" e218edb10161 runoob/ubuntu:v2
# 说明
-m:提交的描述信息
-a:指定镜像作者
e218edb10161：容器ID
runoob/ubuntu:v2:指定要创建的目标镜像名

```

容器操作

> container 容器文件, image文件生成的实例本身也是一个文件,成为容器文件  
也即是说,一旦容器生成,就会存在两个文件:一个image文件,一个容器文件.而且关闭容器并不会删除容器文件,只是容器停止运行而已

```
# 运行容器
docker run httpd
docker container run hello-world

# 输出Hello world
docker run ubuntu:15.10 /bin/echo "Hello world"

# 运行交互式的容器
docker run -i -t ubuntu:15.10 /bin/bash
# 说明
-t:在新容器内指定一个伪终端或终端。
-i:允许你对容器内的标准输入 (STDIN) 进行交互。
ubuntu:15.10 - 使用 ubuntu 基础镜像 15.10
/bin/bash - 运行命令 bash shell
注: ubuntu 会有多个版本，通过指定 tag 来启动特定的版本 [image]:[tag]

# 启动容器（后台模式） -d
docker run -d ubuntu:15.10 /bin/sh -c "while true; do echo hello world; sleep 1; done"

# 命令 --rm 参数,在容器终止运行后自动删除容器文件.
docker container run --rm -p 8000:3000 -it koa-demo /bin/bash

# 重启容器，启动已有的容器，run会再生成一个容器
docker start ID/name
docker container start ID/name


# 停止容器
docker stop ID/name
docker container stop
# 终止容器，直接杀死会丢失数据
docker container kill [container_id]
> 前面的docker container kill命令终止容器的运行,相当于向容器的主进程发送SIGKILL信号,而docker container stop也是用来终止容器的运行,相当于向容器的主进程发送SIGTERM信号,然后过一段时间在发送SIGKILL信号.

# 移除容器
docker rm ID/name
docker container rm [container_id]

# 重命名一个容器
docker rename old_name new_name 

# 查看正在运行的容器
docker ps
CONTAINER ID:容器ID
NAMES:自动分配的容器名称

查看已经启动的容器
docker ps -s 

# 查看已经创建的容器，包括已经停止的容器
docker ps -a

# 查看指定容器的标准输出
docker logs ID/name
docker container logs
> 用来查看容器的输出,即容器里shell的标准输出.比如: 如果docker run命令运行容器的时候,没有使用-it参数,就要使用这个命令查看输出.

# 查看容器的进程
docker top ID/name

查询最后一次创建的容器：
docker ps -l 

# 令容器执行指令
docker exec command
docker container exec command
> 用于进行一个正在运行的容器.如果docker container run命令运行容器的时候,没有使用-it参数,就要使用这个命令进入进入容器,一旦进入容器,就可以在容器的shell执行命令了.
> docker container exec [container_id] /bin/bash

# 从容器中复制文件
docker cp
docker container cp
> docker container cp命令用于从正在运行的容器里,将文件拷贝到本机.下面是拷贝当前 目录的写法:
> docker container cp [container_id]:[/path/to/file] .
```


运行web应用

```
# 载入镜像
docker pull training/webapp
#运行
docker run -d -P training/webapp python app.py
-d:让容器在后台运行。
-P:将容器内部使用的网络端口映射到我们使用的主机上。

# 通过 -p 参数来设置不一样的端口：
docker run -d -p 5000:5000 training/webapp python app.py

# 查看网络端口的快捷方式
docker port bf08b7f2cd89
docker port wizardly_chandrasekhar

查看 WEB 应用程序日志
docker logs [ID或者名字] 可以查看容器内部的标准输出
docker logs -f bf08b7f2cd89
-f: 让 docker logs 像使用 tail -f 一样来输出容器内部的标准输出。

# 检查 WEB 应用程序
使用 docker inspect 来查看 Docker 的底层信息。它会返回一个 JSON 文件记录着 Docker 容器的配置和状态信息。

```
