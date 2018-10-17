# line = int(input("请输入一个数字："))
# while line > 0:
#     tmp = line
#     while tmp > 0:
#         print("*",end="")
#         tmp -= 1
#     print()
#     line -= 1

line = int(input("请输入一个数字："))
while line > 0:
    tmp = line - (line-1)
    while tmp > 0:
        print("*",end="")
        tmp -= 1
    print()
    line -= 1