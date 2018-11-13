# -*- coding: utf-8 -*-
# Time    : 2018/11/13 10:36
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : temp1.py
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
class Bar:
    def foo(self,hobby):
        print("%s,%s岁,%s,%s" % (self.name, self.age, self.sex, hobby))


obj = Bar()
obj.name = '小明'
obj.age = 18
obj.sex = '男'

obj.foo(hobby='上山去打柴')