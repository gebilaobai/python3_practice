# -*- coding: utf-8 -*-
# Time    : 2018/10/27 15:12
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : decorator.py
# Software: PyCharm
import time


# 遵守开放封闭原则
# 装饰器函数实现不修改原函数和调用方式的前提下增加了功能，因为要先加载到内存所以要先放在上面
# def show_time(func):
#     def inner():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print('spend %s' % (end_time - start_time))
#
#     return inner
#
#
# # 原函数
# @show_time  # 等于foo = show_time(foo)
# def foo():
#     print('foo....')
#     time.sleep(2)
#
#
# @show_time  # 等于bar = show_time(bar)
# def bar():
#     print('bar....')
#     time.sleep(1)
#
# foo()
# bar()

# 新需求，在原函数的基础上增加打印函数运行时长的功能
# 很low的方法：修改原函数
# def foo():
#     start_time = time.time()
#     print('foo....')
#     time.sleep(2)
#     end_time = time.time()
#     print('spend %s' % (end_time - start_time))

# 另一种比较low的修改方式：改变了调用方式
# def show_time(func):
#     start_time = time.time()
#     func()
#     end_time = time.time()
#     return end_time - start_time
#
#
# print(show_time(bar))

# 给功能函数加参数
# def show_time(func):
#     def inner(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         end_time = time.time()
#         print('spend %s' % (end_time - start_time))
#
#     return inner
#
#
# @show_time  # 等于foo = show_time(foo)
# def add(*args, **kwargs):
#     sum1 = 0
#     for i in args:
#         sum1 += i
#     print(sum1)
#     time.sleep(1)
#
#
# add(1, 2, 3, 4, 5)


# 装饰器加参数
def logger(flag=''):

    def show_time(func):
        def inner(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            print('spend %s' % (end_time - start_time))
            if flag == 'y':
                print('hi neoby')
            else:
                print('fucker')

        return inner

    return show_time


@logger('y')  # 等于foo = show_time(foo)
def add(*args, **kwargs):
    sum1 = 0
    for i in args:
        sum1 += i
    print(sum1)
    time.sleep(1)


@logger()
def bar():
    print('bar.....')
    time.sleep(1)


add(1, 2, 3, 4, 5)

# bar()
