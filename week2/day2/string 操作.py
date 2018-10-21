# -*- coding: utf-8 -*-
# Time    : 2018/10/21 9:10
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : string 操作.py
# Software: PyCharm

# String 操作


# print('hello'*20)

# print('helloworld'[2:])

# print('el' in 'hello')
#
# print('alex is a good teacher')
# print('%s is a good teacher'%'neoby')
#
#
# a = '123'
# b = 'abc'
# c = a + b
# print(c)
#
# d = ''.join([a,b])
# print(d)

# python 的内置方法
# st='hello kitty {name} is {age}'
st = 'hello kitty {name} is {age}'

# print(st.count('l')) # 统计元素个数，计数
# print(st.capitalize()) # 把首字母大写
# print(st.center(50,'-')) # 居中
# print(st.endswith('y')) # 判断是否以某个内容结尾
# print(st.startswith('h')) # 判断是否以某个内容开头
# print(st.expandtabs(tabsize=10)) # 指定\t的数量
# print(st.find('t')) # 在字符串中查找到第一个元素并返回其索引值，找不到的时候返回-1
# print(st.format(name='NeoBY',age=31)) # 通过变量赋值的方式格式化输出
# print(st.format_map({'name':'NeoBY','age':33})) # 通过字典作为参数进行格式化输出
# print(st.index('t')) # 在字符串中查找到第一个元素并返回其索引值,找不到的时候报出错误
# print('abc456'.isalnum()) # 判断字符串是否是字母数值型 返回 True
# print('abc'.isalnum()) # 判断字符串是否是字母数值型 返回 True
# print('（）'.isalnum()) # 判断字符串是否是字母数值型 返回 False
# print('123456'.isdecimal()) # 判断字符串是不是一个十进制的数 返回 True 非十进制的数返回False
# print('abc456'.isalpha()) # 判断字符串是不是一个纯字符类型的，如果是返回True 如果不是返回False
# print('456'.isdigit()) # 判断字符串是不是一个整型类型的，如果是返回True 如果不是返回False
# print('456.456'.isnumeric()) # 判断字符串是不是一个整型类型的，如果是返回True 如果不是返回False  和.isdigit有点类似
# print('34abc'.isidentifier()) # 判断字符串是否是一个非法标识符
# print('abc'.islower()) # 判断字符串是否全是小写字符
# print('abc'.isupper()) # 判断字符串是否全是大写字符
# print(' '.isspace()) # 判断字符串是不是空格
# print('My Title'.istitle()) # 判断字符串是不是title类型（每个单词首字母大写）
# print(''.join(['A', 'B']))  # 链接任意数量的字符串，被调用的方法的字符串被插入到每个给定的字符串之间。结果作为一个新字符串返回。
# print('ABC'.lower())  # 将字符串中的所有大写变小写
# print('abc'.upper())  # 将字符串中的所有小写变大写
# print('My Title'.swapcase())  # 将字符串中的所有大小写反转
# print('My Title'.ljust(50, '@'))  # 靠左，右侧用指定字符和长度填充
# print('My Title'.rjust(50, '@'))  # 靠右，左侧用指定字符和长度填充
# print('\tMy Title  \n '.strip())  # 将开头结尾的空格和换行符去掉
# print('OK')
# print('\tMy Title  \n '.lstrip())  # 将右侧结尾的空格和换行符去掉
# print('\tMy Title  \n '.rstrip())  # 将左侧开头结尾的空格和换行符去掉
# print('My Title Title'.replace('Title', 'lesson', 1))  # 把字符串中的一部分内容替换成新内容
# print('My Title Title'.rfind('t',))  # 查找字符串中指定的字符中索引位置最高的那个
# print('My Title Title'.split(' '))  # 使用指定内容从左对字符串进行分隔并得到一个list，第二个参数表示分隔几次
# print('My Title Title'.rsplit('i', 1))  # 使用指定内容从右开始对字符串进行分隔并得到一个list，第二个参数表示分隔几次
# print('My Title Title'.title())  # 将字符串以title的格式输出（每个单词首字母大写）

# 摘一些重要的字符串方法
# 1 print(st.count('l'))
# print(st.center(50,'#'))   #  居中
# print(st.startswith('he')) #  判断是否以某个内容开头
# print(st.find('t'))
# print(st.format(name='alex',age=37))  # 格式化输出的另一种方式   待定：?:{}
# print('My tLtle'.lower())
# print('My tLtle'.upper())
# print('\tMy tLtle\n'.strip())
# print('My title title'.replace('itle','lesson',1))
# print('My title title'.split('i',1))
