# -*- coding: utf-8 -*-
# Time    : 2018/11/14 22:26
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 练习.py
# Software: PyCharm


# ##################################定义实现功能的类#############################
class Person:
    def __init__(self,n,g,a,f):
        self.name = n
        self.age = a
        self.gender = g
        self.fight = f

    def grassland(self):
        """注释：草丛战斗，消耗200战斗力"""
        self.fight -= 200

    def practrice(self):
        """注释：自我修炼，增长100战斗力"""
        self.fight += 100

    def incest(self):
        """注释：多人战斗，消耗500战斗力"""
        self.fight -= 500

    def detail(self):
        """注释：当前对象的详细情况"""
        temp = "姓名：%s ; 性别：%s ； 年龄：%s ； 战斗力：%s" % (self.name, self.gender, self.age, self.fight)
        print(temp)

# #################################开始游戏######################################

# ming = Person('鸣人','男',18,1000)
# zuo = Person('佐助','男',19,1800)
# ying = Person('小樱','女',17,2500)
#
# print(ying.fight)
#
# # 输出所有人的详细情况
# ming.detail()
# zuo.detail()
# ying.detail()
#
# ming.grassland() # 鸣人进行了一次草地战斗
# zuo.incest()# 佐助进行了一次个人修炼
# ying.incest()# 小樱进行了一次多人战斗
#
# # 输出所有人的详细情况
# ming.detail()
# zuo.detail()
# ying.detail()


msg ='''
    ——————您想让他做什么——————
    1、进行草地战斗
    2、进行个人修炼
    3、进行多人战斗
    4、不玩了
    —————————————————————————
    '''

y_n = input('是否创建角色？')
if y_n == 'y':
    name = input('请输入姓名')
    age = input('请输入年龄')
    gender = input('请输入性别')
    fight = int(input('请输入战斗力'))

    role = Person(name,gender,age,fight)
    role.detail()

    print(msg)
    flag = True
    while flag and role.fight > 0:
        chooice = int(input('请输入您的选择'))
        if chooice == 1:
            role.grassland()
            role.detail()
        elif chooice == 2:
            role.practrice()
            role.detail()
        elif chooice == 3:
            role.incest()
            role.detail()
        elif chooice == 4:
            flag = False
        else:
            print('请重新输入')
    else:
        print('游戏结束')
else:
    print('游戏结束')
