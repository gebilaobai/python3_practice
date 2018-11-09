# -*- coding: utf-8 -*-
# Time    : 2018/11/8 0:47
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : JSON_loads.py
# Software: PyCharm

import json

f = open('JSON_text','r')
data = f.read()
print(data)
print(type(data))
data = json.loads(data)
print(data)
print(type(data))
