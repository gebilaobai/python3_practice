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
# 1 1 2 3 5 8 13 21 34 55
# 递归实现
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(8))


