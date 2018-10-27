# -*- coding: utf-8 -*-
# Time    : 2018/10/27 15:12
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : decorator.py
# Software: PyCharm
import time


# 遵守开放封闭原则

# 原函数
def foo():
    print('foo....')
    time.sleep(2)


def bar():
    print('bar....')
    time.sleep(1)


# 新需求，在原函数的基础上增加打印函数运行时长的功能
# 很low的方法：修改原函数
# def foo():
#     start_time = time.time()
#     print('foo....')
#     time.sleep(2)
#     end_time = time.time()
#     print('spend %s' % (end_time - start_time))

# 另一种比较low的修改方式：改变了调用方式
def show_time(func):
    start_time = time.time()
    func()
    end_time = time.time()
    return end_time - start_time


print(show_time(bar))
