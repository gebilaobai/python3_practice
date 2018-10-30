# -*- coding: utf-8 -*-
# Time    : 2018/10/30 17:11
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : random模块.py
# Software: PyCharm

import random

# print(random.random())  # 0~1的随机数
# print(random.randint(1, 8))  # 指定随机数的范围，包括右
#
# print(random.choice('hello'))
# print(random.choice(['123',4,[1,2]]))
#
# a = [1,2,3,4,5]
# random.shuffle(a)  # 方法将序列的所有元素随机排序，洗牌功能
# print(a)
#
# print(random.sample(['123',4,[1,2]],2))  # 从序列中选取指定数量的内容
#
# print(random.randrange(1,3))  # # 指定随机数的范围，不包括右


# 随机数例子验证码,比较挫的实现方法
# def v_code():
#     code = ''
#     for i in range(5):
#         if i == random.randint(0,3):
#             add = random.randrange(10)
#         else:
#             add = chr(random.randrange(65,91))
#         code += str(add)
#
#     print(code)

# 比较给力的实现方法
def v_code():
    code = ''
    for i in range(5):
        add = random.choice([random.randrange(10),chr(random.randrange(65,91))])
        code += str(add)

    print(code)


v_code()
