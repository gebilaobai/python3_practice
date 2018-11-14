# -*- coding: utf-8 -*-
# Time    : 2018/11/13 23:21
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 继承.py
# Software: PyCharm

# 继承
class GrandFather:
    def drink_beer(self):
        pass


class Father(GrandFather):  # 父类、基类
    def basktball(self):
        pass

    def football(self):
        pass

    def somke(self):
        print("I like smoke")

    def drink(self):
        print("I like drink")


class Son(Father):  # 子类、派生类
    def driver(self):
        pass

    def somke(self):  # ★★★重写★★★
        print("I don't like smoke")


s = Son()
s.somke()
s.drink()
