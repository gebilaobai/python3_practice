# -*- coding: utf-8 -*-
# Time    : 2018/12/4 23:00
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : metaclass.py
# Software: PyCharm

"""
metaclass,类的祖宗
a.python中一切事物都是对象
b.
    class Foo:
        pass

    obj = Foo()
    # obj是对象
    # Foo类也是一个对象，type的对象

c.
    类都是type类的对象 type(...)
    “对象”都是类的对象 类()
"""


# # 第一种方法 普通方式
# class Foo:
#     def func(self):
#         print(123)
#
#
# # 第二种方法 特殊方式（type类的构造函数）
# def function(self):
#     print(123)
#
# # type('Foo1', (object,), {'func': function}) 声明一个类，类中有一个成员func
# Foo1 = type('Foo1', (object,), {'func': function})
# type第一个参数：类名
# type第二个参数：当前类的基类
# type第三个参数：类的成员
# # 以上两种方式都是声明了一个类

class MyType(type):
    def __init__(self, *args, **kwargs):
        # self = Foo
        print("我是MyType的init方法")
        pass

    def __call__(self, *args, **kwargs):
        # self = Foo
        print('我是Mytype的call方法')
        r = self.__new__()


class Foo(object, metaclass=MyType):
    def __init__(self, *args, **kwargs):
        print("我是Foo的init方法")
        pass

    def __new__(cls, *args, **kwargs):
        return '对象'

    def func(self):
        print('hello Neoby')


obj = Foo()


# 或者看这个例子
# http://www.cnblogs.com/wupeiqi/p/4766801.html
# class MyType(type):
#
#     def __init__(self, what, bases=None, dict=None):
#         super(MyType, self).__init__(what, bases, dict)
#
#     def __call__(self, *args, **kwargs):
#         obj = self.__new__(self, *args, **kwargs)
#
#         self.__init__(obj)
#
# class Foo(object):
#
#     __metaclass__ = MyType
#
#     def __init__(self, name):
#         self.name = name
#
#     def __new__(cls, *args, **kwargs):
#         return object.__new__(cls, *args, **kwargs)
#
# # 第一阶段：解释器从上到下执行代码创建Foo类
# # 第二阶段：通过Foo类创建obj对象
# obj = Foo()