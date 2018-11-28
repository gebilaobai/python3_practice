# -*- coding: utf-8 -*-
# Time    : 2018/11/28 15:00
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 利用属性实现分页.py
# Software: PyCharm


# # 最low的通过列表切片方式实现
# li = []
# for i in range(1000):
#     li.append(i)
#
# while True:
#     p = int(input('请输入要查看的页码：'))  # 第一页 ，每页显示10条
#
#     # 1 0,10
#     # 2 10,20
#     # 3 20,30
#     start = (p-1) * 10
#     end = p * 10
#     print(li[start:end])


# 通过类 属性实现
class Pergination:

    def __init__(self, current_page):
        try:
            p = int(current_page)
        except Exception as e:
            p = 1

        self.page = p
    @property
    def start(self):
        val = (self.page - 1) * 10
        return val
    @property
    def end(self):
        val = self.page * 10
        return val


li = []
for i in range(1000):
    li.append(i)

while True:
    p = input('请输入要查看的页码：')  # 第一页 ，每页显示10条
    obj = Pergination(p)
    # print(li[obj.start():obj.end()])   # 未增加@property时，采用该写法实现，需要增加括号
    print(li[obj.start:obj.end])    # 增加@property后，采用该写法实现，可以不需要括号
