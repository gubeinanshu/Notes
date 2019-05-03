参考： https://blog.csdn.net/Airuio/article/details/80417569

# \_\_file__

> 当前路径

# \_\_doc__

```
class Foo:
    """ 描述类信息，这是用于看片的神奇 """
 
    def func(self):
        pass
 
print Foo.__doc__
#输出：类的描述信息
```

# \_\_str__

> 如果一个类中定义了__str__方法，那么在打印 对象 时，默认输出该方法的返回值

```
class Foo:
 
    def __str__(self):
        return 'alex li'
 
obj = Foo()
print obj
# 输出：alex li
```

# \_\_module__

> 如果当前模块为顶层模块执行 则打印__main__  
如果当前模块为被调用模块的时候 打印当前模块的名称

```
def fun():
    pass

print(fun.__module__)
```

# \_\_name__

> 打印函数名称

```
def fun():
    pass

print(fun.__name__)
```

# \_\_class__

> 表示当前操作的对象的类是什么

```
from lib.aa import C

obj = C()
print obj.__module__  # 输出 lib.aa，即：输出模块
print obj.__class__      # 输出 lib.aa.C，即：输出类
```

# \_\_init__

> 构造方法，通过类创建对象时，自动触发执行

```
class Role(object):    
#初始化函数，在生成一个角色时要    初始化的一些属性就填写在这里    
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        
#__init__中的第一个参数self,和这里的self都 是什么意思？ 看下面解释
self.name = name
        self.role = role
```

#  \_\_del__()

> 析构方法，当对象在内存中被释放时，自动触发执行

```
class Role(object):
    def __init__(self,name,role,weapon:
        self.name = name
        self.role = role
        self.weapon = weapon

    def __del__(self):             #析构函数
        print("del.....run...")
r1 = Role('Alex','police','AK47')    #生成一个角色
```

#  \_\_call__()

```
#所有的函数都是可调用对象。
#一个类实例也可以变成一个可调用对象，特殊方法__call__()。
# 让调用更简单

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print 'My name is %s...' % self.name
        print 'My friend is %s...' % friend
```
```
现在可以对 Person 实例直接调用：

>>> p = Person('Bob', 'male')
>>> p('Tim')
My name is Bob...
My friend is Tim...
```

# \_\_dict__

> 查看类或对象中的所有成员

```
print(类.__dict__) # 打印类里所有属性，不包括实例属性
print(实例.__dict__) #打印实例所有属性，不包括类属性
```

# \_\_slots__

> 可以限制 class的属性

参考： [[Python] dir() 与 __dict__，__slots__ 的区别](https://www.cnblogs.com/ifantastic/p/3768415.html)

[使用__slots__](https://www.liaoxuefeng.com/wiki/897692888725344/923030542875328)

> 在默认情况下，Python 的新类和旧类的实例都有一个字典来存储属性值。这对于那些没什么实例属性的对象来说太浪费空间了，当需要创建大量实例的时候，这个问题变得尤为突出。  
　　因此这种默认做法可以通过在新式类中定义一个 __slots__ 属性从而得到解决。__slots__ 声明中包含若干实例变量，并为每个实例预留恰好足够的空间来保存每个变量，因为没有为每个实例都创建一个字典，从而节省空间。



# \_\_getattr__

> 当访问object不存在的属性时会调用该方法

```
定义了__getattr__()，当访问object不存在的属性时会调用该方法

不定义访问不存在的属性时会报 AttributeError

eg:

class Cat(object):
　　def __init__(self):
　　　　self.name = "jn"

　　def __getattr__(self, item):
　　　　return "tm"


cat = Cat()
print(cat.name)
print(getattr(cat, 'name'))
print("*" * 20)
print(cat.age)
print(getattr(cat, 'age'))
```

# \_\_setattr__

> 当设置类实例属性时自动调用，如j.name=5 就会调用__setattr__方法 

```
class Dict(dict):

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

d = Dict(a=1, b=2)
print (d['a'])
print (d.a) #调用类中原本没有定义的属性时候，调用__getattr__
d.a = 100 #对实例的属性进行赋值的时候调用__setattr__
print (d['a'])
```


# \_\_getattribute__

> 当每次调用属性时，python会无条件进入__getattribute__中，不论属性存在与否，这就是与__getattr__的区别 

> 必须特别小心 getattribute() 方法，因为 Python 在查找类的方法名称时也将对其进行调用。


# \_\_getitem__、\_\_setitem__、\_\_delitem__

> 用于索引操作，如字典。以上分别表示获取、设置、删除数据

```
class Foo(object):
 
    def __getitem__(self, key):
        print('__getitem__',key)
 
    def __setitem__(self, key, value):
        print('__setitem__',key,value)
 
    def __delitem__(self, key):
        print('__delitem__',key)

obj = Foo()
 
result = obj['k1']      # 自动触发执行 __getitem__
obj['k2'] = 'alex'   # 自动触发执行 __setitem__
del obj['k1']
```

# \_\_get__,\_\_set__,\_\_delete__

> 属性描述符的原理利用的是抽象的方法， 把十几个字段共同的特性抽出来

```
class Int_validation:
    def __get__(self, instance, owner):
        return  self.value
    def __set__(self, instance, value):
        if  isinstance(value,int) and 0<value<100:
            self.value=value        #这个要注意 要用value，不能用instance 否则会陷入死循环
        else:
            print("请输入合法的数字")
    def __delete__(self, instance):
        pass

class Student:
    age=Int_validation()

stu=Student()   
stu.age=50
print(stu.age)

```


# \_\_new__/\_\_metaclass__ *（自定义类）

参考： https://www.jianshu.com/p/224ffcb8e73e

> __new__:是用来创建实例的，对类实例化之前进行定制，可以用到。  
__metaclass__：定义一个类如何被创建  
类的生成 调用 顺序依次是 __new__ --> __init__ --> __call__

```
#创建类特殊方式
def func(self):
    print(self.name,self.age)

def __init__(self,name,age):
    self.name = name
    self.age = age

#通过Type实例化产生的Foo类，Foo是Type的对象。
#(object，)加入“,”是为了让括号知道他是个元组。
#type第一个参数：类名
#type第二个参数：当前类的基类
#type第三个参数：类的成员
Foo = type('Foo',(object,),{'talk':func,
                            '__init__':__init__})

f= Foo("Chrn",22)
f.talk()
print(type(Foo))
#Type 为 类的类，所有类都是Type创建的
```

```
class Metaclass(type):
    def __new__(cls, name, bases, dct):
        print 'HAHAHA'
        dct['a'] = 1
        return type.__new__(cls, name, bases, dct)

print 'before Create OBJ'
class OBJ(object):
    __metaclass__ = Metaclass
print 'after Create OBJ'

if __name__ == '__main__':
    print OBJ.a
```


# \_\_add__

> 对象相加直接执行


```
class foo:
def __init__(self,name,age):
self.name=name
self.age=age
def __add__(self, other):
        temp="%s-%d"%(self.name,other.age)
return temp

obj1=foo("aaa",123)#对象1
obj2=foo("bbb",455)#对象2
print("对象1",obj1)
print("对象2",obj2)
print('---自动执行add方法--------')
ret=obj1+obj2 #self代表obj1，other代表obj2
print("add方法",ret)
```

# \_\_iter__

> 生成器作用，返回值可以被迭代，需要使用for执行iter方法

```
class foo:
def __iter__(self):
return iter([11,22,33,44,55])

obj=foo()
for item in obj:#for默认执行iter方法，拿到返回值，for需要一个可以被循环的东西（obj）
    print(item)
```
