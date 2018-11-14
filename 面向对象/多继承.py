# -*- coding: utf-8 -*-
# Time    : 2018/11/14 21:28
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 多继承.py
# Software: PyCharm
"""
在python中支持多继承
    a、左侧优先
    b、一条道走到黑
    c、若有同一个根时，根最后执行

"""




class Father1:
    def football(self):
        print('I like football')


class Father2:
    def football(self):
        print("I don't like basketball")
        self.football()


class Son(Father1, Father2):
    def driver(self):
        print('I like driver')


obj = Son()
obj.driver()
obj.football()
obj.football()