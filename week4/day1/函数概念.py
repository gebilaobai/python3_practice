# -*- coding: utf-8 -*-
# Time    : 2018/10/24 23:16
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 函数概念.py
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


# 例1 打开文件写日志的功能提成函数+在logger函数中增加时间输出
import time

def logger(n):
    # 在日志函数的基础上扩展增加日志中时间的输出
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open('log.txt','a') as f:
        f.write('%s end action%s\n'% (time_current,n))

def action1(n):
    print('starting action%s...'% n)
    logger(n)

def action2(n):
    print('starting action%s...'% n)
    logger(n)

def action3(n):
    print('starting action%s...'% n)
    logger(n)

action1(111)
action2(222)
action3(333)






