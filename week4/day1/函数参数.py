# -*- coding: utf-8 -*-
# Time    : 2018/10/25 14:00
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 函数参数.py
# @Software: PyCharm


# def print_info(name,age):
#     print('Name is: %s'%name)
#     print('Age is: %d'%age)
#
# print_info('baiy',18) # 必需参数
# print_info(age=44,name='alex') # 关键字参数



# 默认参数 在定义函数的时候可以真的某个常用的参数这只一个值，调用时可以自动带出
# def print_info(name,age,sex='male'):
#     print('Name is: %s'%name)
#     print('Age is: %d'%age)
#     print('Sex is: %s'%sex)
#
# print_info('xiaohu',40)
# print_info('jinxing',42)
# print_info('wuchao',12)
# print_info('xiaoya',30,'fmale')

# 不定项参数参数区域通过 *args 表示
# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
# add(1,2,3,4,5,6,7,8,9,10)
#
# def print_info(**kwargs):
#     print(kwargs)
#     for i in kwargs:
#         print('%s is:%s'%(i,kwargs[i]))
# print_info(job='IT',hobby = 'girls',height=188)
#
# def f(*args,**kwargs):
#     pass
# f(1,2,3,[1,2,3],name='baiy',age=31)
#
# # 不定长参数的位置关系:*args放在左边，*kwargs参数放在右边,如果有默认参数放在左边
# def f1(name,sex,*args,**kwargs):
#     pass
# f1('baiy','male',111,222,333,[111,222],hobby='game')

"""
关键参数的优先级最高，默认参数放在关键关键参数后面，不定项参数放在后面
例如：def func(name,age=22,*args,**kwargs)

"""

