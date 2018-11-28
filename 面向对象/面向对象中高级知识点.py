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

# @property 既有方法的影子又有字段的特性
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


# property 练习
"""
有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！
还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：
"""
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60 # ok，实际转化为s.set_score(60)
print('s.score =', s.score) # ok,实际转化为s.get_score()

"""
注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
"""
import datetime as dt
class Student1(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        now_year = dt.datetime.today().year # 获取当前年份
        return now_year - self._birth
# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。

s1 = Student1()
s1.birth = 1986
print(s1.birth)
print(s1.age)

"""
小结
@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
练习
请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
"""

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')