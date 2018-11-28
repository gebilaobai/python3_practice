# -*- coding: utf-8 -*-
# Time    : 2018/11/28 18:08
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 成员修饰符.py
# Software: PyCharm

"""
一、成员修饰符
    共有成员
    私有成员：__字段名
        -无法直接访问，只能间接访问
"""
# 共有、私有字段示例
class Foo:
    def __init__(self, name, age):
        self.name = name    # 共有
        # self.age = age  # 共有
        self.__age = age    # 加__后变成私有的，外界无法直接访问


    def show(self):
        return self.__age

obj = Foo('alex', 19)
print(obj.name)
# print(obj.age)
# print(obj.__age)  # AttributeError: 'Foo' object has no attribute '__age'，无法通过对象直接访问

ret = obj.show()
print(ret)



class Foo2:
    v1 = 'v1'  # 创建了一个共有静态字段
    __v2 = 'v2'

    def __init__(self):
        pass

    def show(self):
        return self.__v2

    @staticmethod
    def stat():
        return Foo2.__v2

print(Foo2.v1)
# print(Foo2.__v2)    # type object 'Foo2' has no attribute '__v2'  不能直接访问
ret = Foo2().show()
print(ret)

print(Foo2.stat())


# 共有、私有方法示例

class Foo3:

    def f1(self):
        return 'f1'

    def __f2(self):
        return 'f2'

    def show(self):
        r = self.__f2()
        return r


obj = Foo3()
ret = obj.f1()
print(ret)

# ret = obj.__f2  # AttributeError: 'Foo3' object has no attribute '__f2'   不能直接访问
# print(ret)

ret = obj.show()
print(ret)


class Father:
    def __init__(self):
        self.father = 'common father'
        self.__father = 'private father'
    def f_show(self):
        r = self.__father
        return r


class Son(Father):
    def __init__(self, name):
        self.name = name
        self.__age = '18'
        super(Son,self).__init__()
    def show(self):
        print(self.name)
        print(self.__age)
        print(self.father)
        # print(self.__father)    # 'Son' object has no attribute '_Son__father'  子类无法直接访问父类中的私有字段
        print(self.f_show())    # 通过父类中间接的方式调用成功

s = Son('NeoBY')
s.show()