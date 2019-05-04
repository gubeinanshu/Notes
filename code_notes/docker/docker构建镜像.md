参考： https://www.jianshu.com/p/1aa13e55c778?utm_campaign=maleskine&utm_content=note&utm_medium=reader_share&utm_source=weibo

[daoCloud平台](https://account.daocloud.io/signin)使用


----------------

> 从容器构建image

1. 先对已经运行的容器进行一些修改，例如 apt update，更新一下软件包
2. commit命令用来将容器转化为镜像，运行下面的命令，我们可以讲刚刚的容器转换为镜像:

```
sudo docker commit -m "Added nginx from ubuntu14.04" -a "saymagic" 79c761f627f3 saymagic/ubuntu-nginx:v1

说明
-m: 参数用来来指定提交的说明信息
-a: 可以指定用户信息的
79c761f627f3: 代表的时容器的id
saymagic/ubuntu-nginx:v1: 指定目标镜像的用户名、仓库名和tag信息。创建成功后会返回这个镜像的ID信息。
注意的是，你一定要将saymagic改为你自己的用户名。因为下文还会用到此用户名
```


> 从dockerfile构建image

1. 进入一个目录，新建目录 www,在其中添加index.html文件


2. 编写dickerfile文件
```
FROM ubuntu:14.04
MAINTAINER zhuzhenyuan zhenyuanzhu@outlook.com
RUN apt-get update
RUN apt-get install -y nginx
COPY ./www /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

# 说明
第一行是用来声明我们的镜像是基于什么构建的，这里我们指定为ubuntu14.04 
第二行的作用在于告诉别人你的大名。
第三行和第四行的RUN命令用来在容器内部的shell里执行命令。
第五行将当前系统的www文件夹拷贝到容器的/usr/share/nginx/html目录下
第六行声明当前需要对外开放80端口
最后一行表示运行容器时开启nginx。
```

> 为什么daemon off;  
docker 容器默认会把容器内部第一个进程，也就是pid=1的程序作为docker容器是否正在运行的依据，如果docker 容器pid挂了，那么docker容器便会直接退出

> docker run的时候把command最为容器内部命令，如果你使用nginx，那么nginx程序将后台运行，这个时候nginx并不是pid为1的程序，而是执行的bash，这个bash执行了nginx指令后就挂了，所以容器也就退出了，和你这个一样的道理，pm2 start 过后，bash 的pid为1，那么此时bash执行完以后会退出，所以容器也就退出了。


3. 构建
```
# 指令
# docker build
# docker image build

示例
docker build -t saymagic/ubuntu-nginx:v2 .
docker build -t="saymagic/ubuntu-nginx:v2" .
docker image build -t koa-demo .
docker image build -t koa-demo:0.0.1 .

# 注意，最后的.表示Dockerfile在当前目录，也可指定其它目录。
# 此时，再次运行docker images就会看到刚刚生成的镜像

```
> 上面代码中,-t参数用来指定image文件的名字,后面还可以用冒号指定标签,如果不指定,默认标签就是latest,最后那个.表示Dockerfile文件所在的路径.这个例子Dockerfile文件在当前路径,所以就是一个.

生成容器
```
$ docker container run -p 8000:3000 -it koa-demo /bin/bash
# 或者
$ docker container run -p 8000:3000 -it koa-demo:0.0.1 /bin/bash
```


> 上传image

发布image文件  
首先，去 hub.docker.com 或 cloud.docker.com注册一个账户。然后，用下面的命令登录

```
docker login
```

接着，为本地的 image 标注用户名和版本。
```
# 设置镜像标签
docker tag [imageName] [username]/[repository]:[tag]
docker image tag [imageName] [username]/[repository]:[tag]

# 实例
docker tag 860c279d2fec runoob/centos:dev
docker image tag koa-demos:0.0.1 ruanyf/koa-demos:0.0.1
```

也可以不标注用户名，重新构建一下 image 文件。重新构建
```
$ docker image build -t [username]/[repository]:[tag] .
```


最后，发布 image 文件。
```
# docker push
docker image push [username]/[repository]:[tag]
```
