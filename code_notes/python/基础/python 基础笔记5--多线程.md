
# 多线程

主线程 创造一个进程的时候，会创造一个线程，这个线程被称为主线程
一个进程里只有一个主线程

注意:
python里的多线程，不是真正意义上的多线程。在任意的指定时间里，有且只有一个线程在运行


使用:
```python

import threading
import time

def test(p):
	time.sleep(0.001)
	print p

ts = []

for i in xrange(0,15):
	th = threading.Thread(target=test,args=[i]) #哪个函数，传入的参数
	th.start()    #启动线程
	ts.append(th) #加入列表

for i in ts:
	i.join() #等待其他线程结束再运行

print "hoho,end!!!!!"

```

## 全局锁（GIL）

是一个很重要的概念。
在任意一个指定的时间，有且只有一个线程在运行 -> python是线程安全的


## io操作用到多线程
必须要lock，acquire release
互斥锁

加锁 acquire
释放锁 release
加锁后 一定要 释放 未释放就成了 死锁

```python
import threading

mlock = threading.RLock()

num = 0
def a():
	global num

	mlock.acquire() #加锁
	num += 1 #你要执行的代码
	mlock.release() #释放锁

	print num

for i in xrange(0,10):
	d = threading.Thread(target=a)
	d.start()
```

## 协程入门

yield 生成器

1.包含yield的函数，则是一个可迭代对象。利用next方法，取每一次的yieldsend
2.生产者，消费者行为
3.无需立刻执行，需要时才执行

```python

def test():
	x = yield '1111111111111'
	print('222222222222%s'%x)
	x = yield '%s,33333333333'%x
	print('444444444444444444%s'%x)
	x = yield '7777777'


t = test()
print(next(t))
print(t.send('5555555555555'))  #这里赋值给第一个x
print(t.send('66666666666666')) #这里给第二个赋值


```






