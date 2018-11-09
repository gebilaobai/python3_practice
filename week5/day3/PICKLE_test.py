# -*- coding: utf-8 -*-
# Time    : 2018/11/8 0:53
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : PICKLE_test.py
# Software: PyCharm

import pickle

def foo():
    print('ok')

dumps_data = pickle.dumps(foo)
print(dumps_data)
print(type(dumps_data))

f = open('PICKLE_text','wb')
f.write(dumps_data)
f.close()



