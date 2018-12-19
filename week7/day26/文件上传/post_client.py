# -*- coding: utf-8 -*-
# Time    : 2018/12/19 14:51
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : post_client.py
# Software: PyCharm

import socket
import os

sk = socket.socket()

address = ('192.168.117.190', 8888)

sk.connect(address)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


while True:
    inp = input('>>>').strip()  # post|11.jpg

    cmd, path = inp.split('|')

    path = os.path.join(BASE_DIR,path)  # 拼接文件的路径

    filename = os.path.basename(path)   # 取到文件名，告诉server如何命名

    file_size = os.stat(path).st_size # 拿到文件的大小

    file_info = 'post|%s|%s' % (filename,file_size)

    sk.sendall(bytes(file_info,'utf-8'))

    f = open(path,'rb')
    has_sent = 0
    while has_sent != file_size:
        data = f.read(1024)
        sk.sendall(data)
        has_sent += len(data)

    f.close()
    print('上传成功~！')






    sk.close()