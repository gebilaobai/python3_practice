# -*- coding: utf-8 -*-
# Time    : 2018/10/26 0:25
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 递归函数.py
# Software: PyCharm

"""
递归函数的特点：
    1、调用自身函数；
    2、需要一个结束条件；
★、但凡是递归可以实现的循环都可以解决；
★、递归的效率在很多时候会很低，

"""


# 思路 n * n-1的阶乘
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)


# # 通过循环实现阶乘
# def f(n):
#     ret = 1
#     for i in range(1,n+1):
#         ret = ret * i
#     return ret
#
# print(f(5))
# for i in range(1,5):
#     print(i)

# 菲波那切数列
# 使用循环实现
def fibo(n):
    before = 0
    after = 1
    before, after = after, after + 1
    return
