# -*- coding: utf-8 -*-
# Time    : 2018/12/4 23:59
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 异常处理.py
# Software: PyCharm

# 最基本的异常处理逻辑
# while True:
#     try:
#         # 代码块，逻辑
#         inp = input('请输入序号：')
#         i = int(inp)
#     except Exception as e:    # 可以捕获所有异常
#         # 上述代码块如果出错了，自动执行当前块的内容
#         # e 是Exception对象，对象中封装了错误信息
#         print(e)
#         i = 1
#
#     print(i)

# li = [11,22]
# li[999] # IndexError
# int('qwe') # ValueError

# try:
#     li = [11, 22]
#     li[999]  # IndexError
#
# except IndexError as e:  # 当出现指定的错误类型如IndexError才进行捕获
#     print('IndexError', e)
# except ValueError as e:
#     print('ValueError', e)
# except Exception as e:
#     print('Exception', e)
# else:
#     print('elese')  # 如果不出错 执行else
# finally:
#     print('。。。')    # finally 不管出不出错都只执行
#


# 主动触发异常,
# try:
#     raise Exception('不过了。。。')
# except Exception as e:
#     print(e)
#
# # 小例子
# def db():
#     return False
#
#
# def index():
#     try:
#         result = db()
#         if not result:
#             # 打开文件写日志
#             # r = open('log', 'a')
#             # r.write('数据库处理错误')
#             raise Exception('数据库处理错误')
#     except Exception as e:
#         str_error = str(e)
#         print(str_error)
#         # 打开文件写日志
#         r = open('log', 'a')
#         r.write(str_error)
#
# index()


# 自定义异常，主要使用__str__方法
#
# class OldBoyError(Exception):
#     def __init__(self, msg):
#         self.message = msg
#
#     def __str__(self):
#         return self.message
#
# # obj = OldBoyError('xxx')
# # print(obj)
#
#
# try:
#     raise OldBoyError('我错了')
# except OldBoyError as e:
#     print(e)

# 断言,用于强制用户服从不服从就报错，并且可被捕获，但一般不进行捕获
# assert 条件
print(123)
assert 1 == 2
print(345)