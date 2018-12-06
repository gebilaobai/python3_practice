# -*- coding: utf-8 -*-
# Time    : 2018/12/5 14:47
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 单例模式.py
# Software: PyCharm
"""
单例模式的一个例子就是数据库连接池
"""



# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age


# obj = Foo() # obj对象，obj也称为Foo类的实例（这个过程叫做实例化）
#
# obj1 = Foo()
# obj2 = Foo()
# obj3 = Foo()

# 单利模式（单个实例），永远使用同一份实例（对象）
# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def show(self):
#         print(self.name,self.age)
#
#
#
# v = None
#
# while True:
#     if v:
#         v.show()
#
#     else:
#         v = Foo('BY',18)
#         v.show()

# 变化一下实现单例模式

class Foo:
    __v = None

    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo()
            return cls.__v

# 不要再使用 类()创建对象
obj = Foo.get_instance()
print(obj)

obj2 = Foo.get_instance()
print(obj2)
