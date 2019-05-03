
# 捕获异常

try:
    pass
except Error:
    pass
fjinally:  #终止行为
    pass

# 引发异常

try:
    raise IndexError #引发异常
except IndexError:
    pass


assert语句也可以用来触发异常，它是一个有条件的raise，主要用在开发过程中调试

assert False, "出错信息"


# 用户自定义的异常
```python
class Bad(Exception):
    pass

def doomed():
    raise Bad()

try:
    doomed()
except Bad:
    print('got Bad')
```
