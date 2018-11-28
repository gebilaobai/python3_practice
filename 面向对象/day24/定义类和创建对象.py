# -*- coding: utf-8 -*-
# Time    : 2018/11/13 10:36
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 定义类和创建对象.py
# Software: PyCharm

"""
示例：用函数实现下列内容
    小明，10岁，男，上山去砍柴
    小明，10岁，男，开车去东北
    小明，10岁，男，最爱大宝剑

    老李，90岁，男，上山去砍柴
    老李，90岁，男，开车去东北
    老李，90岁，男，最爱大宝剑
"""

"""
第一次函数式编程和面向对象的PK：面向对象败下阵来（反而代码量变大了）
"""

# 函数式编程
# def foo(name, age, sex, hobby):
#     print("%s,%s岁,%s,%s" % (name, age, sex, hobby))
#
# foo('小明','10','男','上山去砍柴')
# foo('小明','10','男','开车去东北')
# foo('小明','10','男','最爱大宝剑')
#
# foo('老李','90','男','上山去砍柴')
# foo('老李','90','男','开车去东北')
# foo('老李','90','男','最爱大宝剑')
#
#
# # 面向对象编程
#
# class Bar:
#     def foo(self,name, age, sex, hobby):
#         print("%s,%s岁,%s,%s" % (name, age, sex, hobby))
#
#
# obj = Bar()
# obj.foo('小明','10','男','上山去砍柴')
# obj.foo('小明','10','男','开车去东北')
# obj.foo('小明','10','男','最爱大宝剑')
#
# obj.foo('老李','90','男','上山去砍柴')
# obj.foo('老李','90','男','开车去东北')
# obj.foo('老李','90','男','最爱大宝剑')

"""
一、定义
    函数：
        def + 函数名(参数)
        
    面向对象：
    例如：
    *****************************************************
    class Bar:
    def foo(self,name, age, sex, hobby):
        print("%s,%s岁,%s,%s" % (name, age, sex, hobby))
    *****************************************************        
        class => 名字叫Bar的类
        def   => 名字叫foo的方法
        ####    self  第一个参数必须是self
        
二、执行
    函数：
        函数名(参数)
        
    面向对象：
        o    ——  Bar()  #创建中间人  可以叫对象或实例
        o.foo()
        
三、self()：
        self代指，调用方法的对象（也就是中间人）
        
"""

"""
第二次PK，面向对象做些许改版
"""

# class Bar:
#     def foo(self, hobby):
#         print("%s,%s岁,%s,%s" % (self.name, self.age, self.sex, hobby))
#
#
# obj1 = Bar()
# obj1.name = '小明'
# obj1.age = 18
# obj1.sex = '男'
#
# obj1.foo(hobby='上山去打柴')
#
# obj2 = Bar()
# obj2.name = '老李'
# obj2.age = 90
# obj2.sex = '男'
#
# obj2.foo(hobby='上山去打柴')

"""
构造方法:
    特殊的作用：
        在 obj = 类名()时做了两件事：
            1、创建对象
            2、通过对象执行类中的一个特殊方法__init__构造方法
构造方法的特性：
    类名()自动执行构造方法
"""


class Person:
    def __init__(self, name, age):
        """
        构造方法
        :param name:
        :param age:
        """
        self.n = name
        self.a = age

    def show(self):
        print('%s-%s' % (self.n, self.a))


baiy = Person('白洋', 19)
leib = Person('雷冰', 18)
baiy.show()
leib.show()

"""
总结：
1、如何创建类：
    class 类名:
        pass
        
2、创建方法：
    1、构造方法：__init__(self.arg)
        obj = 类() 创建对象的时候自动执行        
    2、普通方法
        obj = 类('xxx')
        obj.普通方法名()
        
3、面向对象的三大特性之一:封装
    class Bar:
        def __init__(self, n, a)
            self.name = n
            self.age = a
            self.blood = 'o'
    b1 = Bar('alex', 123)
    
    b2 = Bar('eric', 456)
    
    
4、适用场景：
    如果多个函数中有一些相同参数时，可将函数式编程转换成面向对象
"""
