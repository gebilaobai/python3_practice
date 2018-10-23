# -*- coding: utf-8 -*-
# Time    : 2018/10/24 1:11
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 集合.py
# Software: PyCharm

# 集合的创建
"""
1、集合里面的内容会进行去重；
2、集合对象是一组不重复无序排列的可哈希的值:集合成员可以做字典的键
3、集合分类：可变集合：可添加和删除元素，非可哈希的，不能用作字典的键，也不能做其他集合的元素
             不可变集合：与可变集合相反
"""

s = set('apple')
print(s)  # {'e', 'a', 'p', 'l'}

s2 = ['apple', 'banana', 'orange', 'apple']
s3 = set(s2)
print(set(s3))
print(type(s3))
s4 = list(s3)
print(type(s4))
