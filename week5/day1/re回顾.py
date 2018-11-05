# -*- coding: utf-8 -*-
# Time    : 2018/11/5 22:36
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : re回顾.py
# Software: PyCharm

import re
ret = re.findall('a[bc]d', 'abd')
print(ret)

ret = re.findall('www.\w+.com', 'www.baidu.com')
print(ret)

ret = re.findall('www.(\w+).com', 'www.baidu.com')
print(ret)

ret = re.findall('www.(?:\w+).com', 'www.baidu.com')
print(ret)

ret = re.finditer('\d', 'as3sy4784a')
print(ret)
print(next(ret))
print(next(ret).group())