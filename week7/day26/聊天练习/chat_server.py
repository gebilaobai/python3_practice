# -*- coding: utf-8 -*-
# Time    : 2018/12/6 18:11
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : chat_server.py
# Software: PyCharm


import socket

sk = socket.socket()

address = ('192.168.117.190',8888)

sk.bind(address)

sk.listen(2)
print('聊天服务已启动，欢迎加入')

conn, addr = sk.accept()

while True:
    client_data = conn.recv(1023)
    if str(client_data,'utf8') == 'exit':
        break
    print(str(client_data, 'utf8'))
    server_response = input('>>>')
    conn.send(bytes(server_response,'utf8'))

conn.close()


