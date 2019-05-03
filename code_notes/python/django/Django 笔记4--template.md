
# 先看一个例子

```html
<html>
	<head><title>Ordering notice</title></head>
	<body>
		<p>Dear {{ person_name }},</p>
		<p>Thanks for placing an order from {{ company }}. It's scheduled to ship on {{ ship_date|date:"F j, Y" }}.
		</p>
		<p>Here are the items you've ordered:</p>
		<ul>
			{% for item in item_list %}
			<li>{{ item }}</li>
			http://djangobook.py3k.cn/chapter04/[2008-10-14 8:21:10]
			{% endfor %}
		</ul>
		{% if ordered_warranty %}
		<p>Your warranty information will be included in the packaging.</p>
		{% endif %}
		<p>Sincerely,<br />{{ company }}</p>
	</body>
</html>

```
* {{ person_name }} :是 变量(variable)
* { % if ordered_warranty % }  :是 模板标签(templatetag).标签(tag)定义比较明确，即：仅通知模板系统完成某些工作的标签。
* filter :过滤器的例子,它能让你用来转换变量
的输出， 在这个例子中, { { ship_date|date:"F j, Y" } } 将变量 ship_date 用 date 过滤器来转换,转换的参数是 "F j, Y" . date 过滤器根据指定的参数进行格式输 出.过滤器是用管道字符( | )来调用的,就和Unix管道一样.


# 使用模板系统

1. 可以用原始的模板代码字符串创建一个 Template 对象， Django同样支持用指定模板文件路径的方式创建来 Template对象;
2. 调用 Template 对象的 render() 方法并提供给他变量(i.e., 内容). 它将返回一个完整的模板字符串内容,包含了所有标签块与变量解析后的内容.

```python
from django.template import Context, Template

t = Template("My name is {{ name }}.")
c = Context({"name": "Stephane"})
t.render(c)
```
这就是使用Django模板系统的基本规则：写模板，创建 Template 对象，创建 Context ， 调用 render() 方法。

## 句点访问字典中的值

```python
from django.template import Template, Context

person = {'name': 'Sally', 'age': '43'}
t = Template('{{ person.name }} is {{ person.age }} years old.')
c = Context({'person': person})
t.render(c)
```


## 句点调用对象的方法

例如，每个 Python 字符串都有 upper() 和 isdigit() 方法，你在模板中可以使用同样的句点，注意你不能在方法调用中使用圆括号。而且也无法给该方法传递参数；你只能调用不需参数的方法。

```python
from django.template import Template, Context

t = Template('{{ var }} -- {{ var.upper }} -- {{ var.isdigit }}')
t.render(Context({'var': 'hello'}))
t.render(Context({'var': '123'}))
```
若不想模板调用函数，必须设置该方法的 alters_data 函数属性
格式如：函数名.alters_data = True
设置后，模板不会调用该函数，只会安静的失败

## 句点访问列表索引

```python
from django.template import Template, Context

t = Template('Item 2 is {{ items.2 }}.')
c = Context({'items': ['apples', 'bananas', 'carrots']})
t.render(c)
```

不允许使用负数列表索引。像 { { items.-1 } }， 这样的模板变量将会引发TemplateSyntaxError 异常。


## 句点查找可以多级深度嵌套

例如在下面这个例子中 {{person.name.upper}} 会转换成字典类型查找（ person['name']) 然后是方法调用（ upper() )

```python
from django.template import Template, Context

person = {'name': 'Sally', 'age': '43'}
t = Template('{{ person.name.upper }} is {{ person.age }} years old.')
c = Context({'person': person})
t.render(c)
```

## 句点查找规则
可概括为：当模板系统在变量名中遇到点时，按照以下顺序尝试进行查找：

1. 字典类型查找 （比如 foo["bar"] )
2. 属性查找 (比如 foo.bar )
3. 方法调用 （比如 foo.bar() )
4. 列表类型索引查找 (比如 foo[bar] )
系统使用所找到的第一个有效类型。这是一种短路逻辑。





