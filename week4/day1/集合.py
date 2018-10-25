# -*- coding: utf-8 -*-
# Time    : 2018/10/24 1:11
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 集合.py
# Software: PyCharm


"""
1、集合里面的内容会进行去重；
2、集合对象是一组不重复无序排列的可哈希的值:集合成员可以做字典的键
3、集合分类：可变集合(set)：可添加和删除元素，非可哈希的，不能用作字典的键，也不能做其他集合的元素
             不可变集合(frozenset)：与可变集合相反
★★★集合的作用★★★
集合是一个无序的，不重复的数据组合，他的主要作用如下：
1、去重，把一个列表变成集合，就自动去重了
2、关系测试，测试两组数据之前的交集、差集、并集等关系
"""

# s = set('apple')
# print(s)  # {'e', 'a', 'p', 'l'}
#
# s2 = ['apple', 'banana', 'orange', 'apple']
# s3 = set(s2)
# print(set(s3))
# print(type(s3))
# s4 = list(s3)
# print(type(s4))
#
# a = ['apple', 'banana', 'orange', 'apple']
# a2 = frozenset(a)
# print(type(a2))

"""
访问集合
由于集合本身是无序的，所以不能为集合创建索引或切片操作，只能循环遍历或使用in、not in 来访问或判断集合元素。
"""
# print(2 in s)
# print('a' in s)

"""
可变集合的更新
可以使用一下内建方法更新
s.add()
s.update()
s.remove()
s.pop()
s.clear
"""

# set1 = set(['apple'])
# print(set1)
# set1.add('banana')  # 添加一个元素
# print(set1)
# set1.update(['orange'])  # 用所添加的内容和自身的联合更新集合。
# print(set1)
# set1.remove('apple')  # 从集合中删除指定元素
# print(set1)
# set1.pop()  # pop 不需要参数随机删除集合中的一个元素
# print(set1)
# set1.clear()  # 清空集合
# print(set1)
#
# del set1  # 删除集合


"""
集合类型操作符
1、in ,not in
2、集合等价与不等价 == , !=
3、子集、超集
4、联合：联合（union）操作与几何的or操作其实是等价的，联合符号有个等价的方法，union()
5、交集
6、查补
"""

# # 等价、不等价
# s = set('alex')
# s1 = set('alexexex')
# print(s == s1)
# print(s != s1)

a = set([1, 2, 3, 4, 5])
b = set([4, 5, 6, 7, 8])

# 取交集 intersection 也可以用 & 表示
print(a.intersection(b))  # {4, 5}
print(a & b)  # {4, 5}

# 取并集union 也可以用 | 表达
print(a.union(b))  # {1, 2, 3, 4, 5, 6, 7, 8}
print(a | b)

# 差集difference 也可以用 - 表达
print(a.difference(b))  # in a but not in b  {1, 2, 3}
print(a - b)  # in a but not in b  {1, 2, 3}
print(b.difference(a))  # in b but not in a {8, 6, 7}
print(b - a)  # in b but not in a {8, 6, 7}

# 反向交集symmetric_difference 也可以用^表示
print(a.symmetric_difference(b))  # 对称差集{1, 2, 3, 6, 7, 8}
print(a ^ b)  # 对称差集{1, 2, 3, 6, 7, 8}

# 父级 超级 也可用 > 表示
print(a.issuperset(b))  # a 是否完全包涵B
print(a > b)  # a 是否完全包涵B

# 子集
print(a.issubset(b))
print(a <b)


