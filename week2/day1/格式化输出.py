# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 22:24
# @Author  : NeoBY
# @Email   : baiyangbbyy@163.com
# @File    : 格式化输出.py
# Software: PyCharm

name = input("姓名：")
age = input("年龄：")
job = input("工作：")
salary = input("工资：")

if salary.isdigit():  # 判断salary像不像数字
    salary = int(salary)
else:
    print("工资必须输入数字")
    exit()

# msg = '''
#     ------Info of %s------
#     姓名：%s
#     年龄：%s
#     工作：%s
#     工资：%s
#     距离退休还有 %s 年
#     ------end------
#     ''' % (name, name, age, job, salary, 65 - int(age))

msg = '''
    ------Info of %s------
    姓名：%s
    年龄：%d
    工作：%s
    工资：%f
    距离退休还有 %d 年
    ------end------
    ''' % (name, name, age, job, salary, 65 - int(age))

print(msg)

