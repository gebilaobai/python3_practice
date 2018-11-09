# -*- coding: utf-8 -*-
# Time    : 2018/11/9 10:00
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : SHELVE_moudle.py
# Software: PyCharm


import shelve

# 通过shelve创建内容并写入SHELVE_text
f = shelve.open('SHELVE_text')

f['info'] = {'name':'alex','age':'18'}
f['shopping'] = {'name':'alex','price':'-1000'}


# 读取通过shelve创建的内容
data = f.get('info')
print(data)
data = f.get('shopping')
print(data)