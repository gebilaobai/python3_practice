# -*- coding: utf-8 -*-
# Time    : 2018/11/9 10:00
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : SHELVE_moudle.py
# Software: PyCharm

"""
shelve模块比pickle模块简单，只有一个open函数，返回类似字典的对象，可读可写：key必须为字符串，而值可以是python锁支持的数据类型
"""


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



# 补充内容，字典的.get方法
# d = {'name':'alex','age':'18'}
#
# print(d['name'])
#
# print(d.get('name'))
#
# # 如果不加第二个参数就返回原本的，如果有第二个参数就返回第二个参数的值
# print(d.get('sex','male'))