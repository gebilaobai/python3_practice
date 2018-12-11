# -*- coding: utf-8 -*-
# Time    : 2018/12/6 18:12
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : chat_client.py
# Software: PyCharm

import socket

sk = socket.socket()

address = ('192.168.117.190', 8888)

sk.connect(address)
print('欢迎加入隔壁老白的聊天室')
nick_name = input('请输入您的昵称：')
while True:
    inp = input('>>>')
    message =  '%s:%s'%(nick_name, inp)
    sk.send(bytes(message, 'utf8'))
    if inp == 'exit':
        break
    server_response = sk.recv(1024)
    print(str(server_response,'utf8'))
sk.close()

