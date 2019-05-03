
参考: [数据模型参考](http://djangobook.py3k.cn/appendixB/)
# MTV 开发模式

* M 代表模型（Model），即数据存取层。该层处理与数据相关的所有事务：如何存取、如何确认有效性、包含哪些行为以及数据之间的关系等。
* T 代表模板(Template)，即表现层。该层处理与表现相关的决定：如何在页面或其他类型文档中进行显示。
* V 代表视图（View），即业务逻辑层。该层包含存取模型及调取恰当模板的相关逻辑。你可以把它看作模型与模板之间的桥梁。

<!--more-->

# 数据库配置

数据库配置也是在Django的配置文件里，缺省 是 settings.py 。编辑打开这个文件并查找数据库配置：

新版本配置不一样，请另外参考

```python
DATABASE_ENGINE = ''
DATABASE_NAME = ''
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''
```

|  设置  |数据库  |适配器|
|:-------------:|:-------------:|:-----:|
|  postgresql           |PostgreSQL |psycopg 版本 1.x,http://www.djangoproject.com/r/python-pgsql/1/.  |
|  postgresql_psycopg2  |PostgreSQL |psycopg 版本 2.x,http://www.djangoproject.com/r/python-pgsql/.  |
|  mysql                |MySQL      |MySQLdb ,http://www.djangoproject.com/r/python-mysql/.  |
|  sqlite3              |SQLite     |Python 2.5+ 内建。 其他, pysqlite ,http://www.djangoproject.com/r/python-sqlite/.  |
|  ado_mssql            |Microsoft SQLServer |adodbapi 版本 2.0.1+,http://www.djangoproject.com/r/python-ado/.  |
|  oracle               |Oracle     |cx_Oracle ,http://www.djangoproject.com/r/python-oracle/.  |


* DATABASE_NAME 将数据库名称告知 Django 。如果使用 SQLite，请对数据库文件指定完整的文件系统路径。（例如 '/home/django/mydata.db' ）。
* DATABASE_USER 告诉 Django 用哪个用户连接数据库。如果用SQLite，空白即可。
* DATABASE_PASSWORD 告诉Django连接用户的密码。SQLite 用空密码即可。
* DATABASE_HOST 告诉 Django 连接哪一台主机的数据库服务器。如果数据库与 Django 安装于同一台计算机（即本机），可将此项保留空白。使用 SQLite ，也可保留空白。
* DATABASE_PORT 告诉 Django 连接数据库时使用哪个端口。如果用SQLite，空白即可。其他情况下，如果将该项设置保留空白，底层数据库适配器将会连接所给定数据库服务器的缺省端口。在多数情况下，使用缺省端口就可以了，因此你可以将该项设置保留空白。

* 此处的 MySQL 是一个特例。如果使用的是 MySQL 且该项设置值由斜杠（ '/' ）开头，MySQL 将
通过 Unix socket 来连接指定的套接字，例如：
DATABASE_HOST = '/var/run/mysql'
如果用 MySQL 而该项设置的值 不是 以正斜线开始的，系统将假定该项值是主机名。


python manage.py shell 假定你的配置文件就在和 manage.py 一样的目录中。
输入下面这些命令来测试你的数据库配置：
>>> from django.db import connection
>>> cursor = connection.cursor()


# model

新建一个app
python manage.py startapp books
在setting.py中配置好

下面是model例子
```python
from django.db import models

class Publisher(models.Model):
	name = models.CharField(maxlength=30)
	address = models.CharField(maxlength=50)
	city = models.CharField(maxlength=60)
	state_province = models.CharField(maxlength=30)
	country = models.CharField(maxlength=50)
	website = models.URLField()


class Author(models.Model):
	salutation = models.CharField(maxlength=10)
	first_name = models.CharField(maxlength=30)
	last_name = models.CharField(maxlength=40)
	email = models.EmailField()
	headshot = models.ImageField(upload_to='/tmp')


class Book(models.Model):
	title = models.CharField(maxlength=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField()
```


用下面的命令对校验模型的有效性(新版本)
Python manage.py check

python manage.py makemigrations books #用来检测数据库变更和生成数据库迁移文件

python manage.py migrate #用来迁移数据库

python manage.py sqlmigrate books 0001 # 用来把数据库迁移文件转换成数据库语言


# 基本数据访问

## 保存数据

```python
p1 = Publisher(name='Addison-Wesley', address='75 Arlington Street',city='Boston', state_province='MA', country='U.S.A.',website='http://www.oreilly.com/')

p2 = Publisher(name="O'Reilly", address='10 Fawcett St.',city='Cambridge', state_province='MA', country='U.S.A.',website='http://www.oreilly.com/')
p2.save()
publisher_list = Publisher.objects.all()
publisher_list
```
要创建对象，只需 import 相应模型类，并传入每个字段值将其实例化。
调用该对象的 save() 方法，将对象保存到数据库中。Django 会在后台执行一条 INSERT 语句。
使用属性 Publisher.objects 从数据库中获取对象。调用 Publisher.objects.all() 获取数据库中所有的Publisher 对象。此时，Django 在后台执行一条 SELECT SQL语句。



## 添加模块的字符串表现
```python
from django.db import models

class Publisher(models.Model):
	name = models.CharField(maxlength=30)
	address = models.CharField(maxlength=50)
	city = models.CharField(maxlength=60)
	state_province = models.CharField(maxlength=30)
	country = models.CharField(maxlength=50)
	website = models.URLField()

	def __str__(self):
		return self.name
```
就象你看到的一样， __str__() 方法返回一个字符串。 __str__() 必须返回字符串， 如果是其他类型，Python将会抛出TypeError 错误消息 "__str__ returned non-string" 出来。



## 插入和更新数据

```python
#直接改，保存即可
p.name = 'Apress Publishing'
p.save()
```


## 选择对象

我们已经知道查找所有数据的方法了：

ublisher.objects.all()

这相当于这个SQL语句：

SELECT
id, name, address, city, state_province, country, website
FROM book_publisher;

注意
注意到Django在选择所有数据时并没有使用 SELECT* ，而是显式列出了所有字段。 就是这样设计的： SELECT* 会更慢，而且最重要的是列出所有字段遵循了Python 界的一个信条：明确比不明确好。
有关Python之禅(戒律) :-），在Python提示行输入 import this 试试看。

让我们来仔细看看 Publisher.objects.all() 这行的每个部分：
首先，我们有一个已定义的模型 Publisher 。

其次， objects 是干什么的？技术上，它是一个 管理器（manager）。管理器 将在附录B详细
描述，在这里你只要知道它处理有关数据表的操作，特别是数据查找。所有的模型都自动拥有一个 objects 管理器；你可以在想要查找数据时是使用它。

最后，还有 all() 方法。这是 objects 管理器返回所有记录的一个方法。 尽管这个对象 看起来象一个列表（list），它实际是一个 QuerySet 对象， 这个对象是数据库中一些记录的集合。附录C将详细描述QuerySet，现在，我们 就先当它是一个仿真列表对象好了。


## 数据过滤

如果想要获得数据的一个子集，我们可以使用 filter() 方法：(相当于sql中的where)
Publisher.objects.filter(name="Apress Publishing")


你可以传递多个参数到 filter() 来缩小选取范围：(会被转换成and连接)
Publisher.objects.filter(country="U.S.A.", state_province="CA")


注意，SQL缺省的 = 操作符是精确匹配的，其他的查找类型如下：
Publisher.objects.filter(name__contains="press")

在 name 和 contains 之间有双下划线。象Python自己一样，Django也使用 双下划线来做一些小魔法，这个 __contains 部分会被Django转换成 LIKE SQL语句

其他的一些查找类型有： icontains (大小写无关的 LIKE ), startswith 和 endswith , 还有 range (SQL BETWEEN 查询）。 附录C详细列出了这些类型的详细资料。



## 获取单个对象


有时你只想获取单个对象，这个时候使用 get() 方法：
Publisher.objects.get(name="Apress Publishing")

这样，就返回了单个对象，而不是列表（更准确的说，QuerySet)。 所以，如果结果是多个对象，会导致抛出异常
如果查询没有返回结果也会抛出异常


## 数据排序

用 order_by() 来 排列返回的数据
Publisher.objects.order_by("name")

可以对任意字段进行排序
Publisher.objects.order_by("address")

多个字段也没问题
Publisher.objects.order_by("state_provice", "address")

我们还可以指定逆向排序，在前面加一个减号 - 前缀
Publisher.objects.order_by("-name")


每次都要用 order_by() 显得有点啰嗦。 大多数时间你通常只会对某些 字段进行排序。在这种情况下，Django让你可以指定
模型的缺省排序方式：

```python
class Publisher(models.Model):
	name = models.CharField(maxlength=30)
	address = models.CharField(maxlength=50)
	city = models.CharField(maxlength=60)
	state_province = models.CharField(maxlength=30)
	country = models.CharField(maxlength=50)
	website = models.URLField()

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["name"]

```
这个 ordering = ["name"] 告诉Django如果没有显示提供 order_by() , 就缺省按名称

Django使用内部类Meta存放用于附加描述该模型的元数据。 这个类完全可以不实现，不过他能做很多非常有用的事情。查看最上面的参考链接，在Meta项下面，获得更多选项信息，


## 排序

可以同时做这 过滤和排序
Publisher.objects.filter(country="U.S.A.").order_by("-name")

## 限制返回的数据

另一个常用的需求就是取出固定数目的记录。想象一下你有成千上万的出版商在你的数据库里， 但是你只想显示第一个。你可以这样做

Publisher.objects.all()[0]
参考： [数据库api参考](http://djangobook.py3k.cn/appendixC/)


## 删除对象

要删除对象，只需简单的调用对象的 delete() 方法
p = Publisher.objects.get(name="Addison-Wesley")
p.delete()

还可以批量删除对象，通过对查询的结果调用 delete() 方法
publishers = Publisher.objects.all()
publishers.delete()

注意
删除是 不可恢复 的，所以要小心操作！事实上，应该尽量避免删除对象，除非你 确实需要删除它。数据库的数据恢复的功能通常不太好，而从备份数据恢复是很痛苦的。通常更好的方法是给你的数据模型添加激活标志。你可以只在激活的对象中查找， 对于不需要的对象，将激活字段值设为 False, 而不是删除对象。这样， 如果一旦你认为做错了的话，只需把标志重设回来就可以了。



