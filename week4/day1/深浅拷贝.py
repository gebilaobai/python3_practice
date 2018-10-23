# -*- coding: utf-8 -*-
# Time    : 2018/10/23 23:36
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 深浅拷贝.py
# Software: PyCharm

"""
浅拷贝只拷贝一层
深拷贝克隆一份：深拷贝需要引用copy模块（import copy）
"""

# 不可变类型的拷贝
# a = [1, 'Neo', 'BY']
# # a2 = [1, 'Neo', 'BY']
# # a2[0] = 2
# print(a)
# print(a2)

# a = [1, 'Neo', 'BY']
# a2 = a.copy()
#
# a2[0] = 2
# print(a)
# print(a2)


# 浅拷贝（存在可变类型）
a = [[1, 2], 'Neo', 'BY']
a2 = a.copy()
a3 = a[:]  # 这种写法等同于a2 = a.copy()
print('a=', a)
print('a2=', a2)
print('a3=', a3)

a2[1] = 'linux'
print(a)
print(a2)

a2[0][1] = 3
print(a)
print(a2)

"""
浅拷贝例子：
1、丈夫和妻子共用一个帐户里面的钱
2、丈夫花掉了3千元
3、妻子帐户中对应的余额也减少3千元
"""
# husband = ['baiy', 123, [15000, 9000]]
# wife = husband.copy()
# wife[0] = 'wangjy'
# wife[1] = 456
# husband[2][1] -= 3000
# print(wife)

"""
深拷贝例子：
1、丈夫和妻子共用一个帐户里面的钱
2、丈夫花掉了3千元
3、妻子帐户中对应的余额也减少3千元
4、女儿也使用父亲的帐户，但是是另一个独立的帐户,丈夫的帐户余额与女儿的帐户余额互不影响
"""
import copy

husband = ['baiy', 123, [15000, 9000]]
wife = husband.copy()
daughter = copy.deepcopy(husband)
daughter[0] = 'yiyi'
daughter[1] = 789
wife[0] = 'wangjy'
wife[1] = 456
husband[2][1] -= 3000
print(husband)
print(wife)
print(daughter)
