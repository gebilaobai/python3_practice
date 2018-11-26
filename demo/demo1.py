# 九九乘法表
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print("%d*%d=%-2d" % (j, i, j*i), end=' ')
#         j += 1
#     print()
#     i += 1

"""
简述：这里有四个数字，分别是：1、2、3、4
提问：能组成多少个互不相同且无重复数字的三位数？各是多少？
"""
# 第一种实现方法
tar = [1, 2, 3, 4]
count = 0  # 结果计数
for i in range(len(tar)):  # 最外层循环，确定百位数字
    t1 = tar.copy()  # 操作临时变量，防止改变原始tar的值，影响下次循环
    x = str(t1.pop(i))  # 取出百位数字
    for j in range(len(t1)):  # 循环剩余列表，确定十位和个位
        t2 = t1.copy()  # 操作临时变量，防止改变t1的值，影响下次循环
        y = str(t2.pop(j))  # 取出十位数字
        for k in range(len(t2)):  # 循环剩余列表，确定个位
            print(x + y + str(t2[k]), end='  ')  # 将百位十位和个位拼接，得到一个结果
            count += 1  # 结果计数+1
    print('')  # 百位相同的结果显示为一行，百位数字改变的时候换行
print('最终结果为：%s个' % count)

# 第二种实现方法
tar = [1, 2, 3, 4]
count = 0  # 结果计数
for i in range(len(tar)):
    x = str(tar.pop(i))  # 取出百位数字
    for j in range(len(tar)):
        y = str(tar.pop(j))  # 取出十位数字
        for k in range(len(tar)):
            print(x + y + str(tar[k]), end='  ')  # 将百位十位和个位拼接，得到一个结果
            count += 1  # 结果计数+1
        tar.insert(j, int(y))  # 将拿出的十位数字放回原始列表，防止影响下次循环
    tar.insert(i, int(x))  # 将拿出的百位数字放回原始列表，防止影响下次循环
    print('')  # 百位相同的结果显示为一行，百位数字改变的时候换行
