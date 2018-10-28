# -*- coding: utf-8 -*-
# Time    : 2018/10/28 22:38
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 生成器.py
# Software: PyCharm

s = (x * 2 for x in range(10))
print(s)  # s为返回的生成器对象<generator object <genexpr> at 0x0000000002431ED0>

print(s.__next__())  # 不推荐这种写法

print(next(s))  # 推荐这种写法 等价于s.__next__() 在python2中用这种写法：s.next()



