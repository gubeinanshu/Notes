
参考: [模板标签过滤器参考](http://djangobook.py3k.cn/appendixF/)
使用，模板过滤器是在变量被显示前修改它的值的一个简单方法
```python
{{ name|lower }}

```

过滤器可以被 串联 ,就是说一个过滤器的输出可以被输入到下一个过滤器。
```python
{{ my_text|escape|linebreaks }}
```

有些过滤器有参数。过滤器参数看起来是这样
```python
{{ bio|truncatewords:"30" }}
#这个将显示变量 bio 的前30个词。过滤器参数总是使用双引号标识。
```

其他常见
```python
#date : 按指定的格式字符串参数格式化 date 或者 datetime 对象
{{ pub_date|date:"F j, Y" }}

```
* escape : 转义 &符号，引号，<，> 符号。 这在确保用户提交的数据是有效的XML或XHTML时是非常有用的
* addslashes : 添加反斜杠到任何反斜杠、单引号或者双引号前面。 这在处理包含JavaScript的文本时是非常有用的




