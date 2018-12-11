# -*- coding: utf-8 -*-
# Time    : 2018/12/11 15:17
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : cmd_client.py
# Software: PyCharm

import socket

sk = socket.socket()

address = ('192.168.117.190',8887)

sk.connect(address)

while True:
    inp = input('>>>')
    if inp == 'exit':
        break
    sk.send(bytes(inp, 'utf8'))
    result_len = int(str(sk.recv(1024),'utf8'))
    data = bytes()
    while len(data) != result_len:
        recv = sk.recv(1024)
        data += recv
    print(str(data,'gbk'))
sk.close()