# -*- coding: utf-8 -*-
# Time    : 2018/12/6 15:37
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : client.py
# Software: PyCharm

import socket

# 创建socket对象
sk = socket.socket()

address = ('127.0.0.1', 8888)

sk.connect(address)

data = sk.recv(1024)
print(str(data,'utf8'))