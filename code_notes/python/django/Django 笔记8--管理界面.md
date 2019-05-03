
参考: [进入管理界面]http://blog.csdn.net/chr23899/article/details/51959859)

创建 管理员账号
python manage.py createsuperuser


python manage.py makemigrations 生成迁移文件
python manage.py migrate 来实现迁移

配置
在app下的admin.py完成如下的配置:
```python
from django.contrib import admin
from app.models import GfzNotice

#注册模型
admin.site.register(GfzNotice)
```

## 定制管理界面


```python
class Book(models.Model):
	title = models.CharField(maxlength=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField()

	class Admin:
		list_display = ('title', 'publisher', 'publication_date')
		list_filter = ('publisher', 'publication_date')
		ordering = ('-publication_date',)
		search_fields = ('title',)

```

* list_display 选项控制变更列表所显示的列。缺省情况下变更列表只显示对像包含的 表征字符串。我们在这改变成显示标题，出版商和出版日期。
* list_filter 选项在右边创建一个过滤条。我们允许它按日期过滤（它可以让你只显示过去一周，一个月等等出版的书籍）和按出版商过滤。你可以在管理界面中指定任何域做为过滤器，但是用外键，日期，布尔值和有 choices 属性的域是最适合的。过滤至少显示2个值。
* ordering 选项控制对象在管理界面显示时的排序方式。它是想要按序排列的字段的 列表；前面带减号（-）的按逆序排序。在这个例子中，我们按publication date排序， 最近的排在最前。
* search_fields 选项创建了一个允许搜索文本内容的域。它可以搜索 title 字段中的内容（所以您可以输入 Django 以显示所有题名中包含有 Django 的书籍）。

















