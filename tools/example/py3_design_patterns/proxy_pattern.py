# coding: utf8
"""
代理模式：通过一层间接保护层实现更安全的接口访问

A remote proxy.使得访问远程对象就像本地访问一样，例如网络服务器。隐藏复杂性，使得访问本地远程统一。比如ORM
A virtual proxy。用来实现延迟访问，比如一些需要复杂计算的对象，python里可以实现lazy_property，性能改善
A protection/protective proxy. 控制敏感对象的访问，加上一层保护层，实现安全控制
A smart(reference) proxy. 访问对象时加上一层额外操作，例如引用计数和线程安全检查。weakref.proxy()
"""


class LazyProperty:
    """ 用描述符实现延迟加载的属性 """

    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__

    def __get__(self, obj, cls):
        if not obj:
            return None
        value = self.method(obj)
        print('value {}'.format(value))
        setattr(obj, self.method_name, value)
        return value


class Test:
    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None

    @LazyProperty
    def resource(self):  # 构造函数里没有初始化，第一次访问才会被调用
        print('initializing self._resource which is: {}'.format(self._resource))
        self._resource = tuple(range(5))  # 模拟一个耗时计算
        return self._resource


def main():
    t = Test()
    print(t.x)
    print(t.y)
    # 访问LazyProperty, resource里的print语句只执行一次，实现了延迟加载和一次执行
    print(t.resource)
    print(t.resource)


main()
