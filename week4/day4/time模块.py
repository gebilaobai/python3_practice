# -*- coding: utf-8 -*-
# Time    : 2018/10/30 10:47
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : time模块.py
# Software: PyCharm

import time

print(time.time()) # 时间戳
# time.sleep(3)   # 等待时间
# print(time.clock()) # 计算cpu执行时间 在python3.8中将被弃用
print(time.gmtime()) # UTC世界标准时间
print(time.localtime()) # 本地时间
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 把元组得时间按格式化转换成字符串时间
print(time.strptime('2018-10-30 16:54:38', '%Y-%m-%d %H:%M:%S')) #  字符串时间转换成结构化时间
a = time.strptime('2018-10-30 16:54:38', '%Y-%m-%d %H:%M:%S')
print(a.tm_year) #  转化成结构化时间后可以通过内置方法拿出想要的对应日期、时间数据
print(a.tm_wday)

print(time.ctime())  # 将纪元以来的时间(以秒为单位)转换为本地时间的字符串。例如：Tue Oct 30 17:01:43 2018 已经格式化号的内容
print(time.ctime(3600))

print(time.mktime(a))  # 将结构化时间转化成为时间戳

import datetime
print(datetime.datetime.now())