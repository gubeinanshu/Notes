
# 基本的模板标签


## if/else

格式

```python

{% if today_is_weekend %}
	<p>Welcome to the weekend!</p>
{% else %}
	<p>Get back to work.</p>
{% endif %}

```

1. 在python中空的列表 ( [] )，tuple( () )，字典( {} )，字符串( '' )，零( 0 )，还有 None 对象，在逻辑判断中都为假，其他的情况都为真。
2. { % if % } 标签接受 and ， or 或者 not 关键字来对多个变量做判断 ，或者对变量取反（ not )
3. { % if % } 标签不允许在同一个标签中同时使用 and 和 or ，因为逻辑上可能模糊的
4. 系统不支持用圆括号来组合比较操作。如果你发现需要组合操作，例如组合and 和 or ，可以使用嵌套的 { % if % } 标签
5. 多次使用同一个逻辑操作符是没有问题的，但是不能把不同的操作符组合起来。
6. 没有 { % elif % } 标签，请使用嵌套的 { % if % } 标签来达成同样的效果


## for

格式:
```python

<ul>
{% for athlete in athlete_list %}
	<li>{{ athlete.name }}</li>
{% endfor %}
</ul>

```
给标签增加一个 reversed 使得该列表被反向迭代:
```python
{% for athlete in athlete_list reversed %}
...
{% endfor %}

```
{ % for % } 可以嵌套

Django不支持退出循环操作
Django也不支持continue语句


forloop.counter 总是一个表示当前循环的执行次数的整数计数器。这个计数器是从1开始的，
所以在第一次循环时 forloop.counter 将会被设置为1。

```python

{% for item in todo_list %}
	<p>{{ forloop.counter }}: {{ item }}</p>
{% endfor %}

```
* forloop.counter0 :类似于 forloop.counter ，但是它是从0计数的。第一次执行循环时这个变量会被设置为0。
* forloop.revcounter :是表示循环中剩余项的整型变量。在循环初次执行时 forloop.revcounter 将被设置为序列中项的总数。最后一次循环执行中，这个变量将被置1。
* forloop.revcounter0 :类似于 forloop.revcounter ，但它以0做为结束索引。在第一次执行循环时，该变量会被置为序列的项的个数减1。在最后一次迭代时，该变量为0。
* forloop.first :是一个布尔值。在第一次执行循环时该变量为True，在下面的情形中这个变量是很有用的
* forloop.last :是一个布尔值；在最后一次执行循环时被置为True
* forloop.parentloop :是一个指向当前循环的上一级循环的 forloop 对象的引用（在嵌套循环的情况下）。



## ifequal/ifnotequal


```python

#只有模板变量，字符串，整数和小数可以作为 {% ifequal %} 标签的参数

{% ifequal user currentuser %}
	<h1>Welcome!</h1>
{% endifequal %}

{% ifequal section 'sitenews' %}
	<h1>Site News</h1>
{% endifequal %}

{% ifequal section 'sitenews' %}
	<h1>Site News</h1>
{% else %}
	<h1>No News Here</h1>
{% endifequal %}
```


## 注释

```python
# 只能单行，不能跨行
{# This is a comment #}
```

## 模板加载

在 setting.py 中设置 TEMPLATE_DIRS 属性
例子：(参考，下面有更好的方式)
```python
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime

def current_datetime(request):
	now = datetime.datetime.now()
	t = get_template('current_datetime.html')
	html = t.render(Context({'current_date': now}))
	return HttpResponse(html)
```


render_to_response()

```python

from django.shortcuts import render_to_response
import datetime

def current_datetime(request):
	now = datetime.datetime.now()
	return render_to_response('current_datetime.html', {'current_date': now})

```

locals() 技巧

```python
def current_datetime(request):
	current_date = datetime.datetime.now()
	return render_to_response('current_datetime.html', locals())
```

在此，我们没有像之前那样手工指定 context 字典，而是传入了 locals() 的值，它囊括了函数执行到该时间点时所定义的一
切变量。因此，我们将 current_date 变量重命名为 now ，因为那才是模板所预期的变量名称。在本例中， locals() 并没
有带来多 大 的改进，但是如果有多个模板变量要界定而你又想偷懒，这种技术可以减少一些键盘输入。
使用 locals() 时要注意是它将包括 所有 的局部变量，组成它的变量可能比你想让模板访问的要多。在前例中， locals() 还
包含了 request 。对此如何取舍取决你的应用程序。
最后要考虑的是在你调用 locals() 时，Python 必须得动态创建字典，因此它会带来一点额外的开销。如果手动指定 context
字典，则可以避免这种开销。


## get_template()中使用子目录

把模板存放于模板目录的子目录中是件很轻松的事情。只需在调用 get_template() 时，把子目录名和一条斜杠添加到模板名称之前，如：

t = get_template('dateapp/current_datetime.html')

由于 render_to_response() 只是对 get_template() 的简单封装， 你可以对 render_to_response() 的第一个参数做相同处理。

注意
Windows用户必须使用斜杠而不是反斜杠。 get_template() 假定的是 Unix 风格的文件名符号约定。


## include 模板标签

例子：
```python
{% include 'nav.html' %}
{% include "nav.html" %}
{% include 'includes/nav.html' %}
#下面的例子包含了以变量 template_name 的值为名称的模板内容
{% include template_name %}
```

## 模板继承

第一步是定义 基础模板 ， 该框架之后将由 子模板 所继承。以下是我们目前所讲述范例的基础模板
```python
#所有的 {% block %} 标签告诉模板引擎，子模板可以重载这些部分。
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html lang="en">
<head>
	<title>{% block title %}{% endblock %}</title>
</head>
<body>
	<h1>My helpful timestamp site</h1>
	{% block content %}{% endblock %}
	{% block footer %}
	<hr>
	<p>Thanks for visiting my site.</p>
	{% endblock %}
</body>
</html>


```


现在我们已经有了一个基本模板，我们可以修改 current_datetime.html 模板来 使用它
```python
{% extends "base.html" %}

{% block title %}The current time{% endblock %}

{% block content %}
<p>It is now {{ current_date }}.</p>
{% endblock %}


```


## 使用模板继承的一些诀窍

* 如果在模板中使用 { % extends % } ，必须保证其为模板中的第一个模板标记。否则，模板继承将不起作用。
* 一般来说，基础模板中的 { % block % } 标签越多越好。记住，子模板不必定义父模板中所有的代码块，因此你可以用合理的缺省值对一些代码块进行填充，然后只对子模板所需的代码块进行（重）定义。俗话说，钩子越多越好。
* 如果发觉自己在多个模板之间拷贝代码，你应该考虑将该代码段放置到父模板的某个 { % block % } 中。
* 如果需要获得父模板中代码块的内容，可以使用 {{ block.super }} 变量。如果只想在上级代码块基础上添加内容，而不是全部重载，该变量就显得非常有用了。
* 不可同一个模板中定义多个同名的 { % block % } 。存在这样的限制是因为block 标签的工作方式是双向的。也就是说，block 标签不仅挖了一个要填的坑，也定义了在 父 模板中这个坑所填充的内容。如果模板中出现了两个相同名称的{ % block %  } 标签，父模板将无从得知要使用哪个块的内容。
* { % extends % } 对所传入模板名称使用的加载方法和 get_template() 相同。也就数说，会将模板名称被添加到TEMPLATE_DIRS 设置之后。
* 多数情况下， { % extends % } 的参数应该是字符串，但是如果直到运行时方能确定父模板名，这个参数也可以是个变
量。这使得你能够实现一些很酷的动态功能。

