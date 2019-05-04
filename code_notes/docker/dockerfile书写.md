参考：  
https://www.cnblogs.com/codelove/p/10056866.html

---------------
示例

```
# docker file

FROM node:8.4
COPY . /app
WORKDIR /app
RUN npm install --registry=https://registry.npm.taobao.org
EXPOSE 3000
CMD node demos/01.js

# 说明
From node:8.4 : 该image继承自官方的node image,冒号表示标签,这里表示8.4,即8.4版本的node.
COPY . /app :将当前目录下的所有文件都拷贝到image文件的 /app 目录.
WORKDIR /app : 指定接下来的工作目录为 /app .
RUN npm install：在/app目录下，运行npm install命令安装依赖。注意，安装后所有的依赖，都将打包进入 image 文件。
EXPOSE 3000 : 将容器的3000 端口暴露出来,允许外部连接这个端口.

```


```
1.FROM
FROM 指令用于设置在新映像创建过程期间将使用的容器映像。
格式：FROM 
示例：
FROM nginx
FROM microsoft/dotnet:2.1-aspnetcore-runtime

2.RUN
RUN 指令指定将要运行并捕获到新容器映像中的命令。 这些命令包括安装软件、创建文件和目录，以及创建环境配置等。
格式：
RUN ["", "", ""]
RUN
示例：
RUN apt-get update
RUN mkdir -p /usr/src/redis
RUN apt-get update && apt-get install -y libgdiplus
RUN ["apt-get","install","-y","nginx"]
# 注意：每一个指令都会创建一层，并构成新的镜像。
# 当运行多个指令时，会产生一些非常臃肿、非常多层的镜像，不仅仅增加了构建部署的时间，也很容易出错。
# 因此，在很多情况下，我们可以合并指令并运行，
# 例如：RUN apt-get update && apt-get install -y libgdiplus。
# 在命令过多时，一定要注意格式，比如换行、缩进、注释等，会让维护、排障更为容易，这是一个比较好的习惯。
# 使用换行符时，可能会遇到一些问题，具体可以参阅下节的转义字符。

3.COPY
COPY 指令将文件和目录复制到容器的文件系统。文件和目录需位于相对于 Dockerfile 的路径中。
格式：
COPY
如果源或目标包含空格，请将路径括在方括号和双引号中。
COPY ["", ""]
示例：
COPY . .
COPY nginx.conf /etc/nginx/nginx.conf
COPY . /usr/share/nginx/html
COPY hom* /mydir/

4.ADD
ADD 指令与 COPY 指令非常类似，但它包含更多功能。
除了将文件从主机复制到容器映像，ADD 指令还可以使用 URL 规范从远程位置复制文件。
格式：
ADD<source> <destination>
示例：
ADD https://www.python.org/ftp/python/3.5.1/python-3.5.1.exe /temp/python-3.5.1.exe
此示例会将 Python for Windows下载到容器映像的 c:\temp 目录。

5.WORKDIR
WORKDIR 指令用于为其他 Dockerfile 指令（如 RUN、CMD）设置一个工作目录，并且还设置用于运行容器映像实例的工作目录。
格式：
WORKDIR
示例：
WORKDIR /app

6.CMD
CMD指令用于设置部署容器映像的实例时要运行的默认命令。
例如，如果该容器将承载 NGINX Web 服务器，则 CMD 可能包括用于启动Web服务器的指令，如 nginx.exe。 
如果 Dockerfile 中指定了多个CMD 指令，只会计算最后一个指令。
格式：
CMD ["<executable>", ""]
CMD
示例：
CMD ["c:\\Apache24\\bin\\httpd.exe", "-w"]
CMD c:\\Apache24\\bin\\httpd.exe -w

7.ENTRYPOINT
配置容器启动后执行的命令，并且不可被 docker run 提供的参数覆盖。
每个 Dockerfile 中只能有一个ENTRYPOINT，当指定多个时，只有最后一个起效。
格式：
ENTRYPOINT ["", ""]
示例：
ENTRYPOINT ["dotnet", "Magicodes.Admin.Web.Host.dll"]

CMD和ENTRYPOINT
参考： https://blog.csdn.net/u010900754/article/details/78526443
总结：一般还是会用entrypoint的中括号形式作为docker 容器启动以后的默认执行命令，里面放的是不变的部分，可变部分比如命令参数可以使用cmd的形式提供默认版本，也就是run里面没有任何参数时使用的默认参数。如果我们想用默认参数，就直接run，否则想用其他参数，就run 里面加参数。


8.ENV
ENV命令用于设置环境变量。
这些变量以”key=value”的形式存在，并可以在容器内被脚本或者程序调用。
这个机制给在容器中运行应用带来了极大的便利。
格式：
ENV==...
示例：
ENV VERSION=1.0 DEBUG=on \
NAME="Magicodes"

9.EXPOSE
EXPOSE用来指定端口，使容器内的应用可以通过端口和外界交互。
格式：
EXPOSE
示例：
EXPOSE 80

转义字符
在许多情况下，Dockerfile 指令需要跨多个行；这可通过转义字符完成。
默认 Dockerfile 转义字符是反斜杠 \。 
由于反斜杠在 Windows 中也是一个文件路径分隔符，这可能导致出现问题。

要修改转义字符，必须在 Dockerfile 最开始的行上放置一个转义分析程序指令。 如以下示例所示：

# escape=`

注意，只有两个值可用作转义字符：\ 和 ` 。
```



**优化**

> 下面是一些优化的准则：

* 选择合适的基础镜像

一个合适的基础镜像是指能满足运行应用所需要的最小的镜像，理论上是能用小的就不要用大的，能用轻量的就不要用重量级的，能用性能好的就不要用性能差的。这里有时候还需要考虑那些能够减少我们构建层数的基础镜像。


* 优化指令顺序

Docker会缓存Dockerfile中尚未更改的所有步骤，但是，如果更改任何指令，将重做其后的所有步骤。也就是指令3有变动，那么4、5、6就会重做。因此，我们需要将最不可能产生更改的指令放在前面，按照这个顺序来编写dockerfile指令。这样，在构建过程中，就可以节省很多时间。比如，我们可以把WORKDIR、ENV等命令放前面，COPY、ADD放后面。


* 合并指令

前面我们说到了，每一个指令都会创建一层，并构成新的镜像。当运行多个指令时，会产生一些非常臃肿、非常多层的镜像，不仅仅增加了构建部署的时间，也很容易出错。因此，在很多情况下，我们可以合并指令并运行，

例如：RUN apt-get update && apt-get install -y libgdiplus。

在命令过多时，一定要注意格式，比如换行、缩进、注释等，会让维护、排障更为容易，这是一个比较好的习惯。

 

* 删除多余文件和清理没用的中间结果

这点很易于理解，通常来讲，体积更小，部署更快！因此在构建过程中，我们需要清理那些最终不需要的代码或文件。比如说，临时文件、源代码、缓存等等。

* 使用 .dockerignore

.dockerignore文件用于忽略那些镜像构建时非必须的文件，这些文件可以是开发文档、日志、其他无用的文件。例如

.dockerignore

> 下面的代码表示,这三个路径要排除,不要打包进image文件,如果你没有路径可以排除,这个文件也可以不用建立

```
.git
node_modules
npm-debug.log
```

