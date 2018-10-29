# -*- coding: utf-8 -*-
# Time    : 2018/10/30 0:44
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 迭代器.py
# Software: PyCharm

"""
生成器都是迭代器，迭代器不一定是生成器
list，tuple，dict，string：iterable可迭代对象

什么是迭代器？
    满足两个条件：
        1、有iter方法
        2、有next方法
补充内容：
    for 循环内部三件事：
        1、调用可迭代对象的iter方法，返回一个迭代器对象
        2、不断调用迭代器对象的next方法；
        3、处理StopIteration

我们已经知道，可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型，如list、tuple、dict、set、str等；

一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

可以使用isinstance()判断一个对象是否是Iterable对象：
"""

# l = [1, 2, 3, 4, 5]
#
# d = iter(l)  # <list_iterator object at 0x00000000025166A0>
# print(d)
# print(next(d))




print(isinstance([1,2],list))
