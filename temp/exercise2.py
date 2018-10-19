"""while：99乘法表"""
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%-2d"%(j, i, i * j),end=' ')   # %d： 整数的占位符，'-2'代表靠左对齐，两个占位符
        j += 1
    print()
    i += 1


# """for：99乘法表"""
# for a in range(1,10):
#     for b in range(1,10):
#         print(b,"*",a,"=",a*b,"\t",end="")
#         if a == b:
#             print("")
#             break