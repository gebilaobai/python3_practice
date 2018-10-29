# -*- coding: utf-8 -*-
# Time    : 2018/10/28 22:38
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 生成器.py
# Software: PyCharm
"""
生成器就是一个可迭代对象iterable

生成器的两种创建方式：
    1、通过小括号创建：(x * 2 for x in range(5))
    2、通过yield

补充内容：
for 后面跟可迭代对象
    什么是可迭代对象？
        对象内部有__iter__()方法的是可迭代对象
        可以使用isinstance()判断一个对象是否是Iterable
最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成
generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。


"""

# s = (x * 2 for x in range(5))
# print(s)  # s为返回的生成器对象<generator object <genexpr> at 0x0000000002431ED0>

# print(s.__next__())  # 不推荐这种写法
#
# print(next(s))  # 推荐这种写法 等价于s.__next__() 在python2中用这种写法：s.next()
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))  # 超过生成器能生成的数据范围则提示StopIteration


# 通过for循环从生成器中拿东西
# for i in s:
#     print(i)


# def foo():
#     print('ok1')
#     yield 1
#
#     print('ok2')
#     yield 2


# g = foo()
# print(type(foo()))
# print(g)
#
# next(g)
# next(g)

# for i in foo():
#     print(i)

"""
generator非常强大，如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
比如，著名的菲波那切数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
1,1,2,3,5,8,13,21,34
菲波那切数列用列表生成式写不出来，但是，用函数把它打印出来却很容易

"""

"""
a, b = b, a+b
# 这种赋值，先计算等值 右边 就是 b=1 a+b=1
# 再赋值给a和b，那么 a=1, b=1
#然后就是依次这样

"""

# 通过函数实现菲波那切数列
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

# fib(10)

# 通过生成器实现菲波那切数列
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         # print(b)
#         yield b
#         a, b = b, a + b
#         n = n + 1
#
# g = fib(10)
# print(g)
#
# print(next(g))


# .send的使用
# def bar():
#     print('ok1')
#     count = yield 1
#     print(count)
#
#     print('ok2')
#     yield 2
#
# b = bar()
#
# b.send(None)  # 等同于next(b)   第一次send前如果没有next，只能传一个send(None)
# b.send('eee')


