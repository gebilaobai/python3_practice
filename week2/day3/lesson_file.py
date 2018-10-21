# -*- coding: utf-8 -*-
# Time    : 2018/10/20 14:02
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : lesson_file.py
# Software: PyCharm

# 能调用方法的一定是对象

# f = open('小重山', 'r', encoding='utf8')  # r-读取模式-只读
# f = open('小重山', 'w', encoding='utf8')  # w-写入模式-清空重写
# f = open('小重山', 'a', encoding='utf8')  # w-追加模式-在光标所在的最后位置开始追加


f = open('小重山', 'r', encoding='utf8')
# print(f.read())  # 读取并打印全部
# print(f.read(5))    # 读取并打印参数中指定的字符数
# print(f.readline())     # 读取并打印出单行内容
# print(f.readlines())    # 通过readlines将所读取的文件返回并得到一个列表类型

# 得到readlines返回的列表后可通过for循环打印其内容
for i in f.readlines():
    print(i.strip())    # 通过字符串的strip方法将每行前后的空格和换行去掉

f.close()
