@property

> 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@birth.setter，负责把一个setter方法变成属性赋值

> 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性  下面birth是可读写属性，而age就是一个只读属性
```
class Student(object):
    
    def __init__(self, birth):
        self._birth = birth
    
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value
    
    # 使用时 del Student().birth
    @birth.deleter
    def birth(self):
        del self._birth

    @property
    def age(self):
        return 2014 - self._birth
```

@staticmethod 和 @classmethod

> 使用@staticmethod或@classmethod，就可以不需要实例化，直接类名.方法名()来调用

- @staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。 
- @classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。

> 如果在@staticmethod中要调用到这个类的一些属性方法，只能直接类名.属性名或类名.方法名。   
而@classmethod因为持有cls参数，可以来调用类的属性，类的方法，实例化对象等，避免硬编码。

```
class A(object):  
    bar = 1  
    def foo(self):  
        print 'foo'  

    @staticmethod  
    def static_foo():  
        print 'static_foo'  
        print A.bar  

    @classmethod  
    def class_foo(cls):  
        print 'class_foo'  
        print cls.bar  
        cls().foo()  

A.static_foo()  
A.class_foo()  
```

