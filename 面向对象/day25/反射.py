# -*- coding: utf-8 -*-
# Time    : 2018/12/5 13:43
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 反射.py
# Software: PyCharm

"""
getattr
hasattr
setattr
delattr
通过字符串的形式去操作（增删改查）对象中的成员
反射在模块中也可以使用
"""



class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        return '%s-%s' %(self.name,self.age)

obj = Foo('BY', 18)

# 以字符串的形式去某个对象里面去取某个成员

# b = 'name'

# print(obj.__dict__)
# print(obj.__dict__[b])
#
# if b == 'name':
#     obj.name


# 去什么东西里面获取什么内容getattr
# inp = input('>>>>')
#
# v = getattr(obj,inp)
# print(v)

# func = getattr(obj,'show')
# print(func)
# r = func()
# print(r)



# hasattr(),用来判断对象中有没有该成员
# v = hasattr(obj,'name')
# print(v)
# v1 = hasattr(obj,'name1')
# print(v1)


# setattr()给对象中设置属性和值
# setattr(obj,'sex','F')
# print(obj.sex)

# delattr()删除对象中的成员
# obj.name
# delattr(obj,'name')
# obj.name


# 通过类找其中的成员(类也是对象)

# class Foo1:
#
#     stat = '我是静态字段'
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# r = getattr(Foo1,'stat')
# print(r)


# 反射小例子

#第一种用if实现的比较low的方式
# def f1():
#     return '首页'
#
#
# def f2():
#     return '新闻'
#
#
# def f3():
#     return '精华'
#
#
# inp = input('请输入要查看的URL：')
# if inp == 'f1':
#     print(f1())
# elif inp == 'f2':
#     print(f2())
# elif inp == 'f3':
#     print(f3())
# else:
#     print('输入错误，退出')

# 第二种用反射实现

class URL:
    def f1(self):
        return '首页'

    def f2(self):
        return '新闻'

    def f3(self):
        return '精华'

r = URL()
inp = input('请输入要查看的URL：')
if hasattr(r,inp):
    func = getattr(r,inp)
    result = func()
    print(result)
else:
    print('404')