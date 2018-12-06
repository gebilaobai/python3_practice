# -*- coding: utf-8 -*-
# Time    : 2018/12/5 16:49
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 封装.py
# Software: PyCharm

# class Teacher:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.salary = 1000
#
# class Course:
#     def __init__(self, name, teacher, cost):
#         self.name = name
#         self.teacher = teacher
#         self.cost = cost
#
#     def class_up(self):
#         self.teacher.salary += self.cost
#
#
#
# t1 = Teacher('李杰',8)
# t2 = Teacher('烧饼',9)
# t3 = Teacher('豆饼',10)
#
#
# c1 = Course('linux',t1,1)
# print(c1.name)
# print(c1.teacher.name,c1.teacher.age)
# print(c1.teacher.salary)
# c1.class_up()
# print(c1.teacher.salary)



# 嵌套

class F1:
    def __int__(self):
        self.name = 123


class F2:
    def __init__(self, a):
        self.ff = a

class F3:
    def __init__(self, b):
        self.dd = b

f1 = F1()
f2 = F2(f1)
f3 = F3(f2)

# 找到123并输出
f3.dd.ff.name


