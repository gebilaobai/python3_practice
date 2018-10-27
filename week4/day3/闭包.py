# -*- coding: utf-8 -*-
# Time    : 2018/10/27 14:31
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 闭包.py
# Software: PyCharm

"""
闭包（closure）是函数式编程的重要的语法结构
定义：如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包（closure）
如下实例，inner就是内部函数，inner里引用了外部作用域的变脸x（x在外部作用域outer里面，不是全局作用域），则这个内部函数
inner就是一个闭包。

在稍微讲究一点的解释是，闭包= 内部函数块 + 定义函数时的环境，inner就是函数块，x就是环境，当然这个环境可以有很多，不止一个
简单的x。

用比较容易懂的人话说，就是当某个函数被当成对象返回时，夹带了外部变量，就形成了一个闭包。看例子。

"""


def outer():
    x = 10

    def inner():  # 条件1： inner就是内部函数
        print(x)  # 条件2：x就是外部环境的一个变量

    return inner  # 结论：此时内部函数inner就是一个闭包


# 调用inner
outer()()  # 方法1

f = outer()  # 方法2
f()

# inner()  # 局部变量，全局无法调用




