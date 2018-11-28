# -*- coding: utf-8 -*-
# Time    : 2018/11/13 23:21
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 继承.py
# Software: PyCharm

"""
面向对象三大特性之二：继承

    1、继承

        class 父类：
            pass

        class 子类(父类):
            pass

    2、重写
        防止执行父类中的方法

    3、self永远是执行改方法的调用者

    4、
       super(子类, self).父类中的方法(...)
       父类名.父类中的方法(self,...)



    5、Python中支持多继承

        a. 左侧优先
        b. 一条道走到黑
        c. 同一个根时，根最后执行
"""



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


class GrandSon(Father):
    def somke(self):
        super(GrandSon, self).somke()  # 执行父类（基类）中的该方法
        Father.somke(self)             # 执行父类（基类）中的该方法


s = Son()
s.somke()
s.drink()

"""
self永远指调用方法的调用者
"""
obj = Son()
obj.driver()  # driver中的self是形参，此时代指obj
obj.football()  # football中的self是形参，此时代指obj

grandson = GrandSon()
grandson.somke()
