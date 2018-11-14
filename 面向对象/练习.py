# -*- coding: utf-8 -*-
# Time    : 2018/11/14 22:26
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 练习.py
# Software: PyCharm

class Person:
    def __init__(self,n,a,g,f):
        self.name = n
        self.age = a
        self.gender = g
        self.fight = f


role_list = []
y_n = input('是否创建角色？')
if y_n == 'y':
    name = input('请输入名称')
    age = input('请输入年龄')
    gender = input('请输入性别')
    fight = input('请输入战斗力')

    role_list.append(Person(name,age,gender,fight))
