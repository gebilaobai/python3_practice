# # -*- coding: utf-8 -*-
# # Time    : 2018/9/28 22:52
# # Author  : NeoBY
# # Email   : baiyangbbyy@163.com
# # File    : list.py
# # Software: PyCharm
#
# a = ['wuchao', 'jinxing', 'xiaohu', 'sanpang', 'ligang']
#
# # 切片 查询
# # print(a[1:3])
# # print(a[2:])  # 可以取到最后一个值
# # print(a[0:-1])  # 取到倒数第二个值
# # print(a[0:-1:1])  # 步长为1从左往右一个一个的取
# # print(a[1:-1:2])  # 步长为2从左往右的取
# # print(a[3::-2])  # 步长为2从左往右的取
#
# # 向列表中添加内容 append默认向列表最后进行追加 insert+索引值将内容插入指定的索引位
# # a.append('xuepeng')
# #
# # print(a)
# # a.insert(0, 'NeoBY')
# # print(a)
#
# # 修改 通过切片并赋值操作进行修改
# # a[1:3] = ['NeoBY', 'baiy']
# # print(a)
#
# # 删除
# # remove直接跟要删除的元素本身
# # pop 从列表中移除并返回该索引值项，例如可用一个变量接受
# # del
#
# # a.remove('wuchao')
# # print(a)
# # b = a.pop(0)
# # print(a)
# # print(b)
# del a[0]
# print(a)
# del a
#
# count 方法计算某个元素在列表中出现的次数
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 1, 1, 1, 3, 3, 2, 2, ]
# print(a.count(1))

# extend 方法把一个列表添加到另一个列表中
# a = [1, 2, 3]
# b = [4, 5, 6]
# a.extend(b)
# print(a)
# print(b)


# index方法 根据内容找位置
# a = ['wuchao', 'jinxing', 'xiaohu', 'sanpang', 'ligang']
# print(a.index("jinxing"))

# reverse 方法 反转列表内容
# a = ['wuchao', 'jinxing', 'xiaohu', 'sanpang', 'ligang']
# a.reverse()
# print(a)

# sort 方法 对列表内容进行排序
a = [1, 6, 7, 5, 4, 5, 7, 9]
a.sort(reverse=True)
print(a)
a.clear()