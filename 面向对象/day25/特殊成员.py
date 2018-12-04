# -*- coding: utf-8 -*-
# Time    : 2018/11/28 19:51
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 特殊成员.py
# Software: PyCharm
"""
__init__    构造方法：类()自动执行
__del__     析构方法：对象被销毁时，自动执行
__call__    对象()  或  类()()自动执行
__int__     int(对象)
__str__     str()
__add__
__dice__    将对象中封装的所有内容通过字典的形式返回

__getitem__ 切片（slice类型）或者索引
__setitem__
__delitem__

__iter__

"""


#
#
# class Foo:
#     def __init__(self):
#         print('init')
#
#     def __call__(self, *args, **kwargs):
#         print('call')
#
# obj = Foo()
# obj()
#
# Foo()()
#
#
# s = '123'
#
# i = int(s)
# print(i,type(i))
#
#
# class Foo2:
#     def __init__(self):
#         pass
#
#     def __int__(self):
#         return 1111
#
#     def __str__(self):
#         return 'alex'
#
# obj = Foo2()
# print(obj,type(obj))
#
# # int对象，自动执行对象的__int__方法，并将返回值赋值给int对象
# r = int(obj)
# print(r)
#
# r = str(obj)
# print(r)
#
# # __str__方法实用例子
# class Foo3:
#     def __init__(self,n,a):
#         self.name = n
#         self.age = a
#     def __str__(self):
#         return "%s-%s" %(self.name,self.age)
#
# obj = Foo3('alex',19)
# print(obj)  # 等于print(str(obj))  str(obj)  obj中__str__,并获取其返回值
#
#
#
# class Foo4:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __add__(self, other):
#         # self = obj1(alex,19)
#         # other = obj2(eric,66)
#         # return self.age + other.age
#         return Foo4(obj1.name, other.age)
#
#     def __del__(self):
#         print('析构方法')   # 对象被销毁时，自动执行
#
# obj1 = Foo4('alex',19)
# obj2 = Foo4('eric',66)
#
# # 两个对象相加时，自动执行第一个对象的__add__方法，并且将第二个对象当作参数传递进入
# r = obj1 + obj2
# print(r,type(r))



#
#
# class Foo5:
#     """
#     这个类是干xxxx的
#     """
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#
#
# obj = Foo5('alex', 18)
# d = obj.__dict__    # 将对象中的内容通过字典的形式显示出来
# print(d)
#
# ret = Foo5.__dict__ # 将类中的成员（可见和不可见的）都显示出来
# print(ret)



# li = [11,22,33,44]
#
# r1 = li[3]  # 根据索引取值
# print(r1)
#
# li[3] = 666 # 根据索引给某个位置赋值
#
# del  li[2]  # 根据索引把某个值删掉

# class Foo6:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __getitem__(self, item):
#         # return item + 10
#         # ruguo item是基本类型，int,str ， 那么通过索引获取
#         # 如果itme是slice对象的话，那么进行切片
#         if type(item) == slice:
#             print(item.start)
#             print(item.stop)
#             print(item.step)
#             print('调用者希望内部做【切片】处理')
#         else:
#             print('调用者希望内部做【索引】处理')
#
#         print(item, type(item))
#
#
#
#     def __setitem__(self, key, value):
#         print(key,value)
#
#     def __delitem__(self, key):
#         print(key)
#
#
# li = Foo6('alex', 18)
# r = li[8]   # 自动执行li对象的类中的__getitem__方法，并将中括号中的值作为参数传递给item
# print(r)
#
# li[100] = 'asdf'     # 自动执行li对象的类中的__setitem__方法，并将中括号中的值作为参数传递给key 等号后的值传递给value
#
# del li[999]  # 自动执行li对象的类中的__delitem__方法，并将中括号中的值作为参数传递给key
#
# li[1:4:2]


"""
回顾一下切片
"""
# li1 = []
# for i in range(100):
#     li1.append(i)
# print(li1)
#
# print(li1[:4])
# print(li1[1:4])
# print(li1[1:4:2])

# 可迭代对象
class Foo7:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __iter__(self):
        return [11,22,33]

li = Foo7('neoby', 18)
# 1、执行li对象的类Foo7中的__iter__方法，并获取其返回值
# 2、循环上一步中返回的对象

for i in li:
    print(i)

