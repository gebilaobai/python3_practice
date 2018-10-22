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


# f = open('小重山', 'r', encoding='utf8')
# print(f.read())  # 读取并打印全部
# print(f.read(5))    # 读取并打印参数中指定的字符数
# print(f.readline())     # 读取并打印出单行内容
# print(f.readlines())    # 通过readlines将所读取的文件返回并得到一个列表类型

# 得到readlines返回的列表后可通过for循环打印其内容
# for i in f.readlines():
#     print(i.strip())    # 通过字符串的strip方法将每行前后的空格和换行去掉
# f.close()

# 给指定行后面增加内容练习
# f = open('小重山', 'r', encoding='utf8')

# 方法1
# number = 0
# for i in f.readlines():
#     number += 1
#     if number == 6:
#         i = ''.join([i.strip(), 'NeoBY'])
#     print(i.strip())
# f.close()

# 方法2
# data = f.readlines()
# f.close()
# data.insert(5, 'NeoBY')
# for i in data:
#     print(i.strip())

# 不将文件内容读入内存
# number = 0
# for i in f:  # 这是for循环内部将f对象做成了迭代器，用一个取一个
#     number += 1
#     if number == 6:
#         i = ''.join([i.strip(), 'NeoBY'])
#     print(i.strip())

# .tell 当前光标位置；.seek（）移动当前光标至指定位置
# print(f.tell())
# print(f.read(5))
# print(f.tell())
#
# f.seek(3)
# print(f.read(5))

# 进度条
# import sys, time
# for i in range(30):
#     sys.stdout.write('*')
#     # sys.stdout.flush()
#     time.sleep(0.2)

# .truncate 截断
# f = open('小重山', 'a', encoding='utf8')
# f.truncate(3)

# r+读写模式，w+写读模式，a+追加。。。

# r+模式
# f = open('小重山', 'r+', encoding='utf8')
# print(f.readline())
# f.write('岳飞')   # 在r+ 模式下写入时在最后进行写入操作
# f.close()

# w+ 模式 没搞懂继续研究
# f = open('小重山', 'w+', encoding='utf8')
# print(f.readline())
# f.write('岳飞')
# print(f.tell())
# print(f.readline())
# f.close()

# a+ 模式
# f = open('小重山', 'a+', encoding='utf8')
# print(f.readline())
# print(f.tell())
# f.close()

"""
网上收集的例子说明抽空研究
r 只能读 （带r的文件必须先存在）
r+ 可读可写 不会创建不存在的文件 从顶部开始写 会覆盖之前此位置的内容 
w+ 可读可写 如果文件存在 则覆盖整个文件不存在则创建  //要close 之后才算完成写入
w 只能写 覆盖整个文件 不存在则创建 
a 只能写 从文件底部添加内容 不存在则创建 
a+ 可读可写 从文件顶部读取内容 从文件底部添加内容 不存在则创建
--------------------- 
作者：是世博呀 
来源：CSDN 
原文：https://blog.csdn.net/yinghuo110/article/details/79179165 
"""


# 终极问题——修改
"""
思路为：
1、建立一个读取文件的对象f_read和一个写入文件对象f_write
2、设立一个计数器number
3、循环读f_read中的内容并写入f_write中
4、当计数器到达需要插入的行时，通过更改line内容将更改后的line内容继续写入到f_write中
"""
f_read = open('小重山', 'r', encoding='utf8')
f_write = open('小重山2', 'w', encoding='utf8')

number = 0
for line in f_read:
    number += 1
    if number == 5:
        line = ''.join([line.strip(), 'NeoBY\n'])
    f_write.write(line)
f_read.close()
f_write.close()