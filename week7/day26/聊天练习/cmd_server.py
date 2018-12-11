# -*- coding: utf-8 -*-
# Time    : 2018/12/11 15:17
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : cmd_server.py
# Software: PyCharm

"""
远程执行命令
"""
import subprocess

import socket
sk = socket.socket()

address = ('192.168.117.190',8887)

sk.bind(address)
sk.listen(3)
print('Service started...')

while True:
    conn, addr = sk.accept()
    print(addr)
    while True:
        try:
            data = conn.recv(1024)
        except Exception:
            break
        if not data: break
        print(str(data,'utf8'))

        obj = subprocess.Popen(str(data,'utf8'),shell=True,stdout=subprocess.PIPE)
        cmd_result = obj.stdout.read()
        result_len = len(cmd_result)
        conn.sendall(bytes(str(result_len),'utf8'))
        conn.sendall(cmd_result)
    sk.close()


