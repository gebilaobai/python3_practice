# -*- coding: utf-8 -*-
# Time    : 2018/11/21 17:32
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 面向对象中高级知识点.py
# Software: PyCharm

"""
类成员：
    # 字段
        - 普通字段，保存在对象中,执行只能通过对象访问
        - 静态字段，保存在类中，执行时可以通过对象访问，也可以通过类访问
    # 方法
        - 普通方法，保存在类中，由对象来调用，self => 对象
        - 静态方法，保存在类中，由类直接调用，并且不需要self参数
        -   类方法，保存在类中，由类直接调用，cls=》当前类

###########应用场景：
    + 如果对象中需要保存一些值，执行某功能的时候，需要使用对象中的值 -> 普通方法
    + 不需要任何对象中的值 -> 静态方法
    + 需要使用类方法的时候静态方法都能实现
"""


class Foo:
    def __init__(self, name):
        # 普通字段
        self.name = name



    # 普通方法
    def show(self):
        print(self.name)


obj = Foo('alex')
obj.name # 字段直接访问
obj.show() # 方法要加()访问


# 中国的所有省份，用面向对象知识表示

class Privince:
    # 此处的country属于静态字段，静态字段属于类,内存中只保存一份
    country = '中国'
    def __init__(self, name):
        # 普通字段，普通字段属于对象，创建对象时才存在
        self.name = name


print(Privince.country)

hebei = Privince('河北')
print(hebei.name)
print(hebei.country)



class Foo2:
    # 普通方法
    def bar(self):
        print('bar')

    @staticmethod # 加上@staticmethod表示静态方法，静态方法中的self不是必须的,可以通过对象直接访问，相当于调用函数
    def sta():
        print('sta')

    @staticmethod  # 加上@staticmethod表示静态方法，静态方法中的self不是必须的
    def stat(a1,a2):
        print(a1,a2)

    @classmethod  # 加上@classmethod表示类方法，需要最少一个参数，类方法中的参数规范用cls表示，cls是类名
    def classmd(cls):
        # cls 是类名
        print(cls)
        print('classmd')


obj = Foo2()
obj.bar()   # 用对象调用方法

Foo2.bar(obj)  # 用类调用方法

Foo2.sta()
Foo2.stat('啊1','啊2')

Foo2.classmd()


class Foo3:
    def __init__(self):
        self.name = 'a'

    def bar(self):
        print('bar')

    # 用于执行obj.per 获取值
    @property
    def pre(self):
        print('pre')
        return 1

    # 用于obj.per = 123 进行设置值
    @pre.setter
    def pre(self,val):
        print(val)



obj = Foo3()
r = obj.pre
print(r)

obj.pre = 123
