# -*- coding: utf-8 -*-
# Time    : 2018/10/25 23:24
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 高阶函数.py
# Software: PyCharm
"""
什么是高阶函数：
    把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
tips:
1、函数名可以传给一个变量
2、函数名可以作为函数参数，还可以作为函数的返回值
"""
# 高阶函数
def f(n):
    return n**2
def foo(a,b,func):
    ret = func(a) + func(b)
    return ret

print(foo(1,2,f))

a = f
print(foo(1,2,a))

# 函数名可以作为返回值
def foo3():
    def inner():
        return 8
    return inner
ret =foo3()
print(ret)
print(ret())