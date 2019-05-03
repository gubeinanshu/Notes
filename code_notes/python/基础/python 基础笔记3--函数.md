
# 函数

定义
```python
def a():
    "在这里写函数文档"
    retur 4

print test.__doc__ #输出函数文档
#是class时写在class开头，也可写在整个文件的开头，使用模块名.__doc__方式访问
```

带参数，有默认值
```python
def test(a=4):
    return a

def test3(a,c,d="json"):
    return
test3(2,3,d="xml")
```

```python
global b #在函数中声明全局变量，声明后可以修改全局变量
```

```python
def test1(**kr):
    return kr
print test1(c=1,g=24) #转换成字典输出


def test2(*z):
    return z
print test2(1,2,3,435,[2,3,4]) #转换成元组输出


def test(*z,**kr): #一种用法：可以用于读取多余的参数，保函数运行
    return z,kr

#"**" 字典
#"*"  元组
```


# 函数注意点

* 功能完整
* 异常处理完善
* 参数默认值:更省事，更可配置

```python
 assert add(2,4) == 3     #assert :断言，对函数返回值和类型进行确认

dir(func.__code)__)       #查看该属性拥有的项
func.__code__.co_varnames #查看函数有哪些参数
func.__code__.co_filename #查看该函数来自哪个文件
```

# lambda

1. lambda是一个表达式。
2. 它没有名称，存储的也不是代码块，而是表达式。
3. 它被用作执行很小的功能，不能在里面使用条件语句。


```python
d = lambda x:x+1
print d(2)

d = lambda x:x+1 if x > 0 else "error"

#d = lambda x:列表推导式
d = lambda x:[(x,i) for i in xrange(0,10)]

t = [1,2,3,4,5]
g = filter(lambda x:x > 3,t) #过滤出大于 3 的数字
```

# 函数参数位置：
1. 先是位置匹配的参数
2. 再是关键字匹配的参数
3. 收集匹配的元组参数
4. 收集匹配的关键字参数


