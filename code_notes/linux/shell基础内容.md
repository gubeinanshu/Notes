先放下载链接：

[shell编程（ppt+实例代码）.zip](http://op9kkp3ga.bkt.clouddn.com/blog_source/code/shell/20170526/shell%E7%BC%96%E7%A8%8B%EF%BC%88ppt+%E5%AE%9E%E4%BE%8B%E4%BB%A3%E7%A0%81%EF%BC%89.zip)
[shell编程教程（md文件+image）.zip](http://op9kkp3ga.bkt.clouddn.com/blog_source/code/shell/20170526/shell%E7%BC%96%E7%A8%8B%E6%95%99%E7%A8%8B%EF%BC%88md%E6%96%87%E4%BB%B6+image%EF%BC%89.zip)
[shell编程.pdf](http://op9kkp3ga.bkt.clouddn.com/blog_source/code/shell/20170526/shell%E7%BC%96%E7%A8%8B.pdf)

教程

# shell编程

> bash程序由以下三部分组成：  
> 以“#！”开头指定的解释器，以“#”开头的注释行，其他的都是可执行语句，即程序体。
```bash
#!/bin/bash
```

# 一、shell编程之变量

## bash变量命名规则
* 只能包含字母、数字和下划线，并且不能以数字开头；
* 不应该跟系统中已有的环境变量重名；
* 最好能见名知意

## 1.用户自定义变量

> shell中的变量值都是字符型的，要进行算数运算要通过另外的方式，在后面介绍  

### 定义变量

>格式：变量名=变量值 
 
举例：
  
	x=5  
	name="zhu"

### 变量调用：

>echo ${变量名}(推荐)或者echo $变量名  


举例：

	echo ${x}或者$x
	echo ${name}或者$name

## 2.bash环境变量

> 与用户自定义变量区别：  
> 用户自定义变量：  
> 是局部变量，只在当前的Shell中生效  
> 环境变量：  
> 是全局变量，在在当前Shell和这个Shell的所有子Shell中生效  
> 对系统生效的环境变量名和变量作用是固定的

### 设置环境变量

> export 变量名=变量值  
> 或  
> 变量名=变量值  
> export 变量名

### 查看环境变量

* set :查看所有变量
* env :查看环境变量

### 删除环境变量

* unset 变量名

### 常用环境变量

* HOSTNAME :主机名
* SHELL :当前的shell
* TERM :终端环境
* HISTSIZE :历史命令条数
* SSH_CLIENT :当前操作环境是用ssh连接的，这里记录客户端ip
* SSH_TTY :ssh连接的终端时pts/1
* USER :当前登录的用户

### PATH环境变量

> PATH变量：系统查找命令的路径

	echo $PATH #查看PATH环境变量
	PATH="$PATH":/root/sh #增加PATH变量的值


## 3.bash语系变量  

> locale : 查询当前系统语系  
> - LANG :定义系统主语系的变量
> - LC_ALL :定义整体语系的变量

	echo $LANG #查看系统当前语系
	locale -a | more #查看Linux支持的所有语系

### 查询系统默认语系
> 使用以下命令查看配置文件

	cat /etc/sysconfig/i18n


## 4.位置参数变量

### 位置参数变量

![](https://ws1.sinaimg.cn/large/006FdlxCgy1fonasngna6j30ig09owf5.jpg)

举例:新建一个文件名为 a.sh,将以下程序写入文件  

	#!/bin/bash
	num1=$1
	num2=$2
	sum=$(( $num1 + $num2 )) #变量sum的和是num1加num2
	echo $sum #打印变量sum的值

> 编辑完成，退出后对文件赋予执行权限  

	chmod 755 a.sh  
	./a.sh 1 2  #执行

## 5.预定义变量

![](https://ws1.sinaimg.cn/large/006FdlxCgy1fonasnlad9j30if09kmxm.jpg)

### 接受键盘输入

![](https://ws1.sinaimg.cn/large/006FdlxCgy1fonasnowh4j30hf07sglv.jpg)
举例:

	#!/bin/bash
	read -p "please input your name: " name
	echo -e "\n"  #使用 -e 选项就能使echo识别"\n"
	echo $name


# 二、shell编程之数值运算

## declare命令

![](https://ws1.sinaimg.cn/large/006FdlxCgy1fonasnzmnuj30i409h0t7.jpg)

### 把变量声明为数值型

举例:

	aa=11
	bb=22
	echo $aa+$bb
	declare -i cc=$aa+$bb
	echo $cc

### 声明数组变量

举例:

	#定义数组
	movie[0]=aa
	movie[1]=bb
	declare -a movie[2]=live
	#查看数组
	echo ${movie}
	echo ${movie[2]}
	echo ${movie[*]}


### 声明环境变量

> declare -x test=123 #和export作用相似，但其实是declare命令的作用  
> set #查看环境变量

## 数值运算方法

> 数值运算方法1:使用declare定义


> 数值运算方法2:使用 expr或let数值运算工具

举例:

	aa=1
	bb=22
	dd=$(expr $aa + $bb) #"+"号左右两侧必须有空格
	echo $dd

> 数值运算方法3:"$((运算式))"（推荐）或者"$[运算式]"

举例：

	aa=1
	bb=3
	cc=$(( $aa+$bb ))
	dd=$[ $aa+$bb ]
	echo $cc
	echo $dd

## 变量测试(了解)

> 变量测试在脚本优化时使用，一般使用者，只要了解即可

![](https://ws1.sinaimg.cn/large/006FdlxCgy1fonaso5y0zj30ii09mgmb.jpg)

# 三、shell编程之条件判断和流程控制
## 1.条件判断式语句

> 两种判断格式  
> test -e /root/install.log  
> [ -e /root/install.log ]

举例：按照

	[ -e /root/install.log ] && echo yes || echo no
	#第一个判断命令如果正确执行，则打印“yes”，否则打印“no”

### 按照文件类型进行判断

![](https://ws1.sinaimg.cn/large/006FdlxCgy1fonasorvecj30fh07y750.jpg)

### 按照文件权限进行判断

![](https://ws1.sinaimg.cn/large/006FdlxCgy1fonasowg5bj30ez07mq3f.jpg)

### 两个文件之间进行比较
![](https://ws1.sinaimg.cn/large/006FdlxCgy1fonaspdjj0j30hr08xdg9.jpg)

### 两个整数之间比较
![](https://ws1.sinaimg.cn/large/006FdlxCgy1fonaspxs1dj30ep07ct94.jpg)

### 字符串的判断
![](https://ws1.sinaimg.cn/large/006FdlxCgy1fonasq1q11j30hz098jrq.jpg)

### 多重条件判断
![](https://ws1.sinaimg.cn/large/006FdlxCgy1fonasq5lbfj30i909e74k.jpg)

## 2.条件判断if语句

### 单分支if语句

> 格式  
> if [ 条件判断式 ];then  
> 　程序  
> fi  
> 或者  
> if [条件判断式 ]  
> 　then  
> fi  
> [ 条件判断式 ]就是使用test命令判断，所以中括号和太监判断式之间必须有空格

### 双分支if语句

> 格式  
> if [ 条件判断式 ]  
> 　then  
> 　　条件成立时，执行程序  
> 　else  
> 　　条件不成立时，执行的另一个程序  
> fi  

### 多分支if语句

> 格式  
> if [ 条件判断式 ]  
> 　then  
> 　　当条件判断式1成立时，执行程序1  
> elif  
> 　then  
> 　　当条件判断式2成立时，执行程序2  
> ...省略更多条件...  
> else  
> 　　当所有条件都不成立时，最后执行此程序  
> fi  

##  3. 多分支case语句

> 格式  
> case $变量名 in  
> 　"")  
> 　　如果变量的值等于1，则执行程序1  
> 　　;;  
> 　"")  
> 　　如果变量的值等于1，则执行程序1  
> 　　;;  
> 　...省略其他分支...  
> 　*)  
> 　　如果变量的值都不是以上的值，则执行此程序  
> 　　;;  
> esac  


##  4. for循环

### 语法一

> 格式  
> for 变量 in 值1 值2 值3...  
> 　do  
> 　　程序  
> 　done  

举例1:

	#!/bin/bash
	for i in 1 2 3 4 5
		do
			echo $i
		done

举例2:

	#!/bin/bash
	#列出当前目录下的文件
	for i in ls
		do
			echo $i
		done

### 语法二

> 格式  
> for (( 初始值;循环控制条件;变量变化 ))  
> 　do  
> 　　程序  
> 　done  

举例:

	#!/bin/bash
	#从1加到100
	s=0
	for(( i=1;i<=100;i=i+1 ))
		do
			s=$(( $s+$i ))
		done
	echo "The sum of 1+2+...+100 is : $s"

##  5. while循环和until循环

> while格式  
> while [ 条件判断式 ]  
> 　do  
> 　　程序  
> 　done  

举例：

	#!/bin/bash
	#从1加到100
	i=1
	s=0
	while [ %i -le 100 ]
	#如果变量i的值小于等于100，则执行循环
		do
			s=$(( $s+$i ))
			i=$(( $i+1 ))
		done
	echo "The sum is: $s"

> until格式  
> until [ 条件判断式 ]  
> 　do  
> 　　程序  
> 　done  

举例:

	#!/bin/bash
	#从1加到100
	i=1
	s=0
	until [ $i -gt 100 ]
	#循环知道变量i的值大于100，就停止循环
		do
			s=$(( $s+$i ))
			i=$(( $i+1 ))
		done
	echo "Teh sum is: $s"

## 6.break命令
> break命令允许跳出所有循环（终止执行后面的所有循环）

举例:

	#!/bin/bash
	while :
	do
		echo -n "输入 1 到 5 之间的数字:"
		read aNum
		case $aNum in
			1|2|3|4|5) echo "你输入的数字为 $aNum!"
			;;
			*) echo "你输入的数字不是 1 到 5 之间的! 游戏结束"
				break
			;;
		esac
	done

执行以上代码，输出结果为：

> 输入 1 到 5 之间的数字:3  
> 你输入的数字为 3!  
> 输入 1 到 5 之间的数字:7  
> 你输入的数字不是 1 到 5 之间的! 游戏结束  

## 7.continue命令

> continue命令与break命令类似，只有一点差别，它不会跳出所有循环，仅仅跳出当前循环

举例:

	#!/bin/bash
	while :
	do
		echo -n "输入 1 到 5 之间的数字:"
		read aNum
		case $aNum in
			1|2|3|4|5) echo "你输入的数字为 $aNum!"
			;;
			*) echo "你输入的数字不是 1 到 5 之间的!"
				continue
				echo "游戏结束"
			;;
		esac
	done
> 运行代码发现，当输入大于5的数字时，该例中的循环不会结束，语句 echo "Game is over!" 永远不会被执行。


# 四、shell程序调试

> Bash常用的调试方法是带-x执行程序，这样会把执行到的语句全部显示出来。  

格式：

> bash -x file.sh

举例:

	...
	set -v
	#需要调试的语句
	set +v
	...


> 如果bash程序很长，可在需要调试的程序块前后标记调试标记—块前插入语句set –v，块后插入语句set+v即可，这样调试时只打印调试块中的执行路径。建议bash程序的语句最好不要超过1000行。






