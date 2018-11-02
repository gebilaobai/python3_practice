# -*- coding: utf-8 -*-
# Time    : 2018/10/30 23:56
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : hashlib_module.py
# Software: PyCharm

import hashlib

m =hashlib.md5()
print(m)

m.update('hello world'.encode('utf8'))

print(m.hexdigest())  # 5eb63bbbe01eeed093cb22bb8f5acdc3

m.update('neoby'.encode('utf8'))
print(m.hexdigest())  # 7e5d1b91146f60ff6b97caa60e835aab

m2 = hashlib.md5()
m2.update('hello worldneoby'.encode('utf8'))
print(m2.hexdigest())  # 7e5d1b91146f60ff6b97caa60e835aab

sha = hashlib.sha256()
print(sha)
sha.update('hello world'.encode('utf8'))
print(sha.hexdigest())