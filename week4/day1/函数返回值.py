# -*- coding: utf-8 -*-
# Time    : 2018/10/25 21:28
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 函数返回值.py
# Software: PyCharm

"""
return的作用：
    1、结束函数；
    2、返回某个对象；
注意点：
    1、函数里如果没有return，默认返回None
    2、如果return多个对象，python会帮我们把多个对象封装成一个元组返回
"""


# 返回什么内容，给谁
# def f():
#     print('ok')
#     return 10
#
#
# a = f()
# print(a)
#
#
# def add(*args):
#     Sum = 0
#     for i in args:
#         Sum += i
#     return Sum  # 返回就算汇总结果
#
#
# print(add(1, 2, 3, 4, 5))

def foo():
    return 1,'123',8,[1,2,3]

print(foo())
print(type(foo()))