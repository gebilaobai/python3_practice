# -*- coding: utf-8 -*-
# Time    : 2018/12/19 14:51
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : post_server.py
# Software: PyCharm

import socket
import os

sk = socket.socket()

address = ('192.168.117.190',8888)

sk.bind(address)
sk.listen(2)
print('文件上传服务器已启动')


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    conn, addr = sk.accept()
    print(addr)

    while True:
        data = conn.recv(1024)

        cmd,filename,filesize = str(data,'utf8').split('|')
        print(cmd,filename,filesize)
        path = os.path.join(BASE_DIR,'yuan',filename)
        filesize = int(filesize)


        f = open(path,'wb')
        has_receive = 0
        while has_receive != filesize:
            data = conn.recv(1024)
            f.write(data)
            has_receive += len(data)
        f.close()






