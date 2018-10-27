# -*- coding: utf-8 -*-
# Time    : 2018/10/26 17:12
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 重要的内置函数.py
# Software: PyCharm


"""
1、filter(function, iterable):
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回
True 的元素放到新列表中。
注意: Pyhton2.7 返回列表，Python3.x 返回迭代器对象
"""

str = ['a', 'b', 'c', 'd']


def fun1(s):
    if s != 'a':
        return s


ret = filter(fun1, str)  # 是一个迭代器对象 <filter object at 0x00000274F11B7208>
print(ret)
print(list(ret))  # 将过滤器对象转换成列表 里面的值为['b', 'c', 'd']

"""
2、map(function, iterable, ...)
map() 会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
参数：
    function -- 函数
    iterable -- 一个或多个序列
返回值：
    Python 2.x 返回列表。
    Python 3.x 返回迭代器。
"""
str2 = ['a', 'b', 'c', 'd']


def fun2(s):
    return s + 'neoBy'


ret2 = map(fun2, str2)
print(ret2)
print(list(ret2))


def square(x):
    return x ** 2


a = map(square, range(1, 101))
print(list(a))

"""
描述
reduce() 函数会对参数序列中元素进行累积。
函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的
第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
语法：
    reduce(function, iterable[, initializer])
参数：
    function -- 函数，有两个参数
    iterable -- 可迭代对象
    initializer -- 可选，初始参数
返回值：
    返回函数计算结果。
"""
from functools import reduce


def add1(x, y):
    return x + y


print(reduce(add1, range(1, 101)))

"""
lambda
匿名函数的命名规则：用lambda关键字标识，冒号（:）左侧表示函数接受的参数（a,b），冒号(:)右侧表示函数的返回值（a+b）。
因为lambda在创建史不需要命名，所以，叫匿名函数。
"""


# 普通函数与匿名函数的对比：
# 普通函数

def add(a, b):
    return a + b


print(add(3, 4))

# 匿名函数
add2 = lambda a, b: a + b

print(add2(2, 3))

# 匿名函数实例1:通过reduce函数加lambda表达式实现阶乘：
from functools import reduce

print(reduce(lambda x,y:x*y,range(1,6)))

# 匿名函数实例2：通过map函数加lambda表达式实现计算平方
squares = map(lambda x : x*x,range(9))
print(squares)
print(list(squares))
