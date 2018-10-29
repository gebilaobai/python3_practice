# -*- coding: utf-8 -*-
# Time    : 2018/10/28 22:38
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 生成器.py
# Software: PyCharm
"""
生成器就是一个可迭代对象iterable
"""



s = (x * 2 for x in range(5))
print(s)  # s为返回的生成器对象<generator object <genexpr> at 0x0000000002431ED0>

# print(s.__next__())  # 不推荐这种写法
#
# print(next(s))  # 推荐这种写法 等价于s.__next__() 在python2中用这种写法：s.next()
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))  # 超过生成器能生成的数据范围则提示StopIteration


# 通过for循环从生成器中拿东西
for i in s:
    print(i)



