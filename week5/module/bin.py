# -*- coding: utf-8 -*-
# Time    : 2018/11/6 23:08
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : bin.py
# Software: PyCharm


# import calculate  # 解释器通过搜索路径找到calculate.py 后，将calculate= calculate.py all code
# print(calculate.add(1, 2))

from week5.module.calculate import *  # 从模块里调用指定方法

print(add(1, 3))
