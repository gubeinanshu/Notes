
1. 如何去定义一个最基本的class
2. class最基本的子元素
3. class传参
4. __init__方法
5. class和函数的区别

# 定义 class
可继承，重写，
```python
# -*- coding: utf-8 -*-
class test(object): #所有的class都是object的派生类

	a = 1 #属性

	#当定义一个class的内置方法时，方法的参数的第一个永远是self。
	def __init__(self,var1): #构造函数
		self.var1 = var1 #这里的 self.var1 为全局变量

	#get被称之为test对象的方法
	def get(self,a=None):
		return self.var1

	def __del__(self): #析构函数
		del self.arg1

	pass


#使用
t = test('test str heiheihei')
print t.get()
```
1. 通过在一个变量或者函数之前加上下划线来表示私有变量的，例如__spam(这里是两个下划线)就是私有的。
2. Python会在类的内部自动的把你定义的__spam变量的名字替换成为 _classname__spam(注意，classname前面是一个下划线，spam前是两个下划线)，Python把这种技术叫做“name mangling”。因此，用户在外部访问__spam的时候就会提示找不到相应的变量。

# 模块

包的创建 :文件夹中创建 __init__.py 文件


搜索模块
```python
import  sys
sys.path.append('/tmp/m2') #添加模块搜索路径
```

下面的含义是: 当前文件作为主函数时执行，其他文件 import 不执行

if __name__ == "__main__":





