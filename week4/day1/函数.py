# -*- coding: utf-8 -*-
# Time    : 2018/10/24 23:16
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 函数.py
# Software: PyCharm

"""
计算机函数 != function
计算机函数 == subroutine 子程序 ，procedures 过程
作用：
    1、减少重复代码
    2、方便修改，更易扩展
    3、保持代码的一致性
定义：
    函数是指将一组语句的集合通过一个名字（函数名）封装起来，要想执行这个函数，只需调用其函数名即可
函数名的命名规则：
    1、函数名必须以下划线或字母开头，可以包含任意字母、数字、下划线的组合，不能使用任何的标点符号；
    2、函数名是区分大小写的。
    3、函数名不能是保留字
"""


def add(a, b):
    print(a + b)


x = int(input("请输入a的值"))
y = int(input("请输入b的值"))
add(x, y)

