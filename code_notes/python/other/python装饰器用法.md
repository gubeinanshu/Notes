参考： https://blog.csdn.net/u013205877/article/details/78872278

一个非常简单的示例

```
def funA(fn):
    print('A')
    fn() # 执行传入的fn参数
    return 'fkit'
'''
下面装饰效果相当于：funA(funB)，
funB将会替换（装饰）成该语句的返回值；
由于funA()函数返回fkit，因此funB就是fkit
'''
@funA
def funB():
    print('B')
print(funB) # fkit
```
上面程序使用 ＠funA 修饰 funB，这意味着程序要完成两步操作：
- 将 funB 作为 funA() 的参数，也就是上面代码中 @funA 相当于执行 funA(funB)。
- 将 funB 替换成上一步执行的结果，funA() 执行完成后返回 fkit，因此 funB 就不再是函数，而是被替换成一个字符串。

> **被修饰的函数总是被替换成 ＠ 符号所引用的函数的返回值，因此被修饰的函数会变成什么，完全由于 ＠ 符号所引用的函数的返回值决定，换句话说，如果 ＠ 符号所引用的函数的返回值是函数，那么被修饰的函数在替换之后还是函数。**



### functools.wraps定义函数装饰器
https://www.cnblogs.com/fcyworld/p/6239951.html

> 装饰器（decorator）是干嘛的？对于受到封装的原函数来说，装饰器能够在那个函数执行前或者执行后分别运行一些代码，使得可以再装饰器里面访问并修改原函数的参数以及返回值，以实现约束定义、调试程序、注册函数等目标。装饰器一般返回一个包装器（wrapper），而functools.wraps就是装饰包装器的装饰器。

```
def tracer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r,%r)->%r'%(func.__name__,args,kwargs,result))
        return result
    return wrapper

@tracer
def fibonacci(n):
    if n in (0,1):
        return n
    return (fibonacci(n-1)+fibonacci(n-2))


fibonacci(3)
print(fibonacci)
print('help:')
help(fibonacci)
```
输出

```
fibonacci((1,),{})->1
fibonacci((0,),{})->0
fibonacci((2,),{})->1
fibonacci((1,),{})->1
fibonacci((3,),{})->2
<function tracer.<locals>.wrapper at 0x0000024BD3A04598>
help:
Help on function wrapper in module __main__:

wrapper(*args, **kwargs)
```


> 装饰器正常工作，但是函数的名字变成装饰器中的包装器了！！！help内置函数也失效了  
也就是说，原函数的属性失效了  
如果想要保留原函数的属性，就可以用到functools.wraps了

加上 @functools.wraps(func)

```
import functools

def tracer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r,%r)->%r'%(func.__name__,args,kwargs,result))
        return result
    return wrapper

@tracer
def fibonacci(n):
    if n in (0,1):
        return n
    return (fibonacci(n-1)+fibonacci(n-2))


fibonacci(3)
print(fibonacci)
print('help:')
help(fibonacci)
```
输出

```
fibonacci((1,),{})->1
fibonacci((0,),{})->0
fibonacci((2,),{})->1
fibonacci((1,),{})->1
fibonacci((3,),{})->2
<function fibonacci at 0x0000026227A54598>
help:
Help on function fibonacci in module __main__:

fibonacci(n)
```
保留原函数的属性


### 类装饰器

```
class decorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('before............')
        res = self.func(*args, **kwargs)
        print('after............')
        return res


@decorator
def run():
    print('run............')

if __name__ == "__main__":
    run()
-----------------------------------
before............
run............
after............

```

### 装饰类

参考： https://www.jianshu.com/p/dd983ecc1104

