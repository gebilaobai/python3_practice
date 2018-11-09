# -*- coding: utf-8 -*-
# Time    : 2018/11/8 1:05
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : PICKLE_loads.py
# Software: PyCharm

import pickle


def foo():
    print('ok')

f = open('PICKLE_text','rb')
data = f.read()
data = pickle.loads(data)

data()
