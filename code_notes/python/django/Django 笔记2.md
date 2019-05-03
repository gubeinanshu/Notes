
# 配置 url
## 第一种方式

直接在工程目录中的 urls.py 文件中添加


## 第二种方式

包含其他 url

1. 在根 urls.py 引入 include
2. 在 app 目录下创建 urls.py 文件，格式与根 urls.py 相同
3. 根 urls.py 中 url 函数第二个参数改为 include('blog.urls')

注意事项

* 根 urls.py 针对 app 配置的 URL 名称，是改 app 所有 URL 的总路径
* 配置 URL 时注意政策表达式结尾符号$和/

# Template

## 开发第一个 Template

步骤
1. 在 app 的根目录下创建名叫 Templates 的目录
2. 在该目录下创建 HTML 文件
3. 在 views.py 中返回 render()

DTL 初步使用

* render() 函数中支持一个 dict 类型参数
* 该字典是后台传递到模板的参数，键位参数名
* 在模板中使用 {{参数名}} 来直接使用

## 注意点
Django 查找 Templates
* 按照INSTALLED_APPS中的添加顺序查找 Templates
* 不同 app 下 Templates 目录中的同名 html 文件会造成冲突

解决方案

* 在 app 的 Templates目录下创建以 app 名为名称的目录，将 html 问价内放入新创建的目录下