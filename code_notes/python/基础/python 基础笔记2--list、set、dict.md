
# list(列表)

1. 有序的集合
2. 通过偏移来索引，从而读取数据
3. 支持嵌套
4. 可变的类型
1. 切片：
a = [1,2,3，4，5，6，7］
正向索引 :a[1:5]
反向索引 :a[-4:-1]
默认索引 :a[:], a[:3], a[1:]

## 添加操作
* '+'生成一个新的列表
* extend() :接受参数并将该参数的每个元素都添加到原有的列表中，原地修改列表而不是新建列表
* append() :添加任意对象到列表的末端
* insert() :插入任意对象到列表中，可以控制插入位置。

## 修改

修改列表本身只需要直接赋值操作就行。
```python
A   = [1,2,3]
A[0]='haha'
```

## 删除操作

* del()   :我们通过索引删除指定位置的元素。
* remove():移除列表中指定值的第一个匹配值。如果没找到的话，会抛异常。
* pop()   :返回最后一个元素，并从list中删除它。

## 成员关系：

In , not in :我们可以判断一个元素是否在列表里。返回一个bool类型，元素在列表里返回true，否则返回fasle.

## 列表推导式

[expr for iter_var in iterable]

1. 首先迭代iterable里所有内容，每一次迭代，都把iterable里相应内容放到iter_var中，再在表达式中应用该iter_var的内容，最后用表达式的计算值生成一个列表。

比如我们要生成一个包含1到10的列表
```python
[x for x in range(1,11)]

Range(1,11)
```

[expr for iter_var in iterable if cond_expr]

2. 加入了判断语句，只有满足条件的内容才把iterable里相应内容放到iter_var中，再在表达式中应用该iter_var的内容，最后用表达式的计算值生成一个列表。

要生成包含1到10的所有奇数列表。
```python
range(1,11,2)

[x for x in range(1,11) if x % 2 == 1]
```

```
[x*x for x in range(100)]

#生成字符串
['the %s'%d for d in xrange(10)]

#生成元组
[(x,y) for x in range(2) for y in range(2)]

#生成字典
dict([(x,y) for x in range(3) for y in range(2)])
```

## 内置list方法
```
list(a) #返回一个列表，参数是可迭代对象，可传入字符串，元组
```
range 返回一个列表对象
xrange 返回xrange对象
上面的区别在python3中已经没有了

del a 删除列表对象的引用
del a[:] 清空列表对象里的元素


## 	排序:sort 翻转:reverse

a = [33,11,22,44]

b = a.sort() #排序，默认从小到大, 返回值为None
b = a. reverse() #反转一个list返回值为none,结合上面从大到小排序

## list 其他操作

```python
b = a[:]  #这样可以拷贝,而不是拷贝引用
````

# 集合

## 创建集合
set():可变的，不可变的frozenset()
## 操作
1. 添加 add，update
2. 删除：remove
3. 交集，并集，差集：& | -
4. 成员关系 in ,  not in
5. set去重，列表内容元素重复
```python
a=[1,2,1,2,12,1,2]
list(set(a)) #这样可以将列表内容去重
```

# 字典

## 创建

{} , dict()
```python
info = {'name':'lilei','age':20}
info = dict(name='lilei',age=20)
```
字典的键必须是不可变的数据类型，比如数字，字符串，元组
binfo = {1:'22',2:'33'}
binfo = {(1,2),'as',(a,b),"df"}

##添加内容
a['xx'] = 'xx'
```python
info['phone'] = 'iphone'
```
## 修改内容
a['xx'] = 'xx'
```python
例如 info['phone'] = 'htc'
```

## update
参数是一个字典的类型，会覆盖相同的值
```python
info.update({'city':'beijing','phone':'nokia'})
```
## 删除清空操作
```python
del info['phone']       #删除某个元素
info.clear()            #删除字典的全部元素
info.pop('name')        #返回值，删除键名
info.pop('name','1234') #name 不存在返回默认值 1234
```

## get
```python
info.get('name')      #没有返回 NoneType 类型
info.get('age2','22') #可以设置默认值
```

## 成员关系操作
in 和has_key()
```python
phone in info
info.has_key('phone')
```
## 其他操作
keys()   :返回的是列表，里面包含了字典的所有键
values() :返回的是列表，里面包含了字典的所有值
items()  :生成一个字典的容器 :[()]

binfo = {'a':[1,2,3],'b':[4,5,6]}
binfo['a'][2] = 5     #修改的方式

字典排序，以键从小到大
```
key_list = a.keys()
key_list.sort()
for x in key_list:
    print x,a[x]
```