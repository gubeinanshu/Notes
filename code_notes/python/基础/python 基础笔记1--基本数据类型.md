
# 基本数据类型

1. int 整型
2. long 长整型
3. float 浮点数
4. boolean 布尔
5. string  字符串
6. list 列表 []
7. tuple 元组 ()
8. dict 字典 {}
9. set 集合
* 不可变类型: int, long, float, string, tuple
* 可变类型:   list, dict, set
* r"" 不转义

# 关于中文

在文件开始添加
```python
# -*- coding: UTF-8 -*-
```

r"" : 字符串不转义

这样定义 utf-8 编码的中文字符串
```python
u"中文"
```
或者
```python
a = "啊啊啊啊"
a.decode('utf-8')  #转换成 utf-8
```

# 有用的函数

| 函数              |  说明                |
|:-----------------:|:--------------------:|
| type()            | 查看变量的数据类型   |
| help()            | 查看帮助文档         |
| id()              | 查看变量 id          |
| dir()             | 查看有哪些方法       |
| len()             | 查看字符串长度       |
| sys.getrefcount   | python内部的引用计数 |

# 关于变量
1. 动态特性 可以赋予不同的数据类型
2. 多重赋值
```python
#下面相当于 a,b,c = ("str","str1",4)
a,b,c = "str","str1",4

del b  #删除变量
```



# print 使用

```python
print "2", 
pirnt "4"
```
上面这样的方式可以将结果输出到一行

重定向写入文件内容
```python
f = open('test.txt',"w")
print >> f,"asdfasdfsf" ,
print >> f,"kljlkjllk"
f.close()
```

# 控制流语句
## if
```python
if True: #条件
	print 4 #执行代码块
else:
	pirnt 代码块

if True:
	print "True"
elif not True:
	print "not True"
else:
	pass #什么都不执行
```
```python
if False:
    print 4
#上面的错
if not True:
    print 4
#这个对
```

## 布尔值的运算符

and 全部都为bool值  
or 至少有一项为bool真  
is 检查共享，检查是否引用同一个对象  
== 检查值  
not 非 

## 三元表达式
```python
4 if True else 3
#相当于
if True:
	print 4
else:
	print 3
```

## while,for
```python
while True:
    print 4
else:
	print '在while正常跑完时执行'
```

break,continue

```python
for x in "i am a man".split(" "):#以空格分隔
    print x
else:
    print '与while相同'
# x保留最后迭代值
```

## or的运用
```python
a = url.get(from) or None #如果前一个为null, 则赋值None
```

## for 使用

```
a = "asdfas"
for i in a:
    print i

b = [1,2,3,4,5]
for i in b:
    pirnt i

c = ('a','b','c')
for i in c:
    print i


#如果定义了重复的键，只取最后一个
a = {'key1':'value1','key2':'value2','key2':'vale3'}

#遍历键
for i in a.keys():
    print i

#同时遍历键值
for x,y in a.items():
    print x,y

```

根据字典的值得到字典的键
1. 字典索引的是键，而不是值->迭代，穷举
2. 字典具有唯一键，单值却不要求是唯一的
3. 一个值可能对应多个键


# 字符串拼接

1. 字符串拼接 "+" 号连接 浪费性能，不推荐
2. 字符串模板
'%s' :字符串占位符
'%d' :整型占位符
```python
"test %s test" % "this"
"test %s test %s" % ("this","that")
```
3. 优秀拼接方案
```
a = 'one'
b = 'two'
c = 'three'
",".join([a,b,c]) #以逗号分隔返回字符串
"".join([a,b,c]) #返回拼接后的字符串
```
4. format使用
```python
#下面 前面的数字对应后面的位置，也可不填数字，此时前后一一对应
a = "test {1} {0} " .format("one" , "two")
#更人性化的方式
a = "test {whose} {fruit} " .format(fruit="one" , whose="two")
```
5. 字典方式
```
a = "test %(whose)s %(fruit)s" % {'whose':'my','fruit':'apple'}
```

# string 操作

字符串替换
```python
a = a.replace("原字符串","目标字符串")
```

```python
import string
g = string.maketrans('123',"abc") #g 为模板
a = '1234567'
print a.translate(g) #根据模板替换
#上面输出为：
#abc4567
#是逐个替换，有对应关系1->a这样
translate(g,'1') #删除字符串中全部的 1
```

字符串查找
```python
a.find("要查询的字符串")    #返回开始的位置
a.find("要查询的字符串",20) #从字符串的20位开始查找
```

字符串排序
```python
a = "234rsDSFJ"
print sorted(a,reverse=True)
print sorted(a,key=string.upper)
```


# 文件操作
```python
d = open('a.txt', w) #打开文件,模式可以是w/r/a
d.write('test,\ntest')
d.close()            #关闭
d.readline()
d.seek(0)            #偏移量移动到开头
d.read(1000)         #读多少个字节
```

```
import linecache
linecache.getline("a.txt",int line) #获取某一行
linecache.getline("a.txt ")         #获取全部
```


# with语句

```
g = open('a.txt'，'w')
g.write("hahhahahahah\nhahah")
g.close()

#下面的代码与上面等同，会自动关闭文件
with open('a.txt','a') as g:
    g.write('xixixi')
```

