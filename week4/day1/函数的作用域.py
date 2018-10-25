# -*- coding: utf-8 -*-
# Time    : 2018/10/25 21:46
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 函数的作用域.py
# Software: PyCharm

"""
python中的作用域分4种情况：
L：local，局部作用域，即函数中敌营的变量：
E：enclosing，嵌套的父级函数的局部作用域，即包含此函数的上级函数的局部作用域，但不是全局的；
G：globa，全部变量，就是模块级别定义的变量
B：built-in，系统固定模块里面的变量，比如int，bytearray等。

搜索变量的优先级顺序依次是：
    作用域局部>外层作用域>当前模块中的全局>python内置作用域，也就是LEGB
"""

# x = int(2.9)  # built-in
# g_count = 0  # global
# def outer():
#     o_count = 1  # enclosing
#
#     def inner():
#         i_count = 2  # local
#         print(i_count)
#     inner()
#
# outer()


# count = 10
#
#
# def outer():
#     # global count
#     count = count + 1
#     print(count)
#
#
# outer()

# a = 1
#
#
# def f1():
#     a = 2  # python默认创建一个局部变量a并赋值2
#     print(a)  # 打印的是局部变量a的值
#
#
# f1()
# print(a)  # 全局变量并未受到局部变量的影响，所以输出的值还是全局变量的值
#
#
# def f2():
#     global a  # 通过使用global生命此处a使用的是全局变量的a
#     a = 2  # 故此处a做的赋值操作实际是对全局变量a进行了重新赋值
#     print(a)  # 此处打印的也是被重新赋值后的全局变量a
#
#
# f2()
# print(a)  # 此处打印的也是被重新赋值后的全局变量a

# unnlocal 非局部的
def outer():
    count = 10
    def inner():
        nonlocal count
        count = 20
        print(count)
    inner()
    print(count)
outer()


"""
小结
1、变量查找顺序：lEGB，作用域局部>外层作用域>当前模块中的全局>python内置作用域；
2、只有模块、类、及函数才能引入新的作用域；
3、对于一个变量，内部作用域先声明就会覆盖外部变量，不声明直接使用，就会使用外部作用域的变量；
4、内部作用域要修改外部作用域变量的值时，全局变量要是用global关键字，嵌套作用域变量要使用nonlocal关键字。nonlocal是
python3新增的关键字，有了这个关键字，就能完美的实现闭包了；
"""

print(c)
c = 100