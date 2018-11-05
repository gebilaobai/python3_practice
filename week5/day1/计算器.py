# -*- coding: utf-8 -*-
# Time    : 2018/11/5 23:12
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 计算器.py
# Software: PyCharm

import re


# source = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

# 格式化字符串
def format_string(string):
    string = string.replace('--', '+')
    string = string.replace('-+', '-')
    string = string.replace('++', '+')
    string = string.replace('+-', '-')
    string = string.replace('*+', '*')
    string = string.replace('/+', '/')
    string = string.replace(' ', '')
    return string


# 检查表达式合法性
def check_expression(string):
    check_result = True
    # 括号是否匹配
    if not string.count('(') == string.count(')'):
        print('表达式错误，括号未闭合！')
        check_result = False
    if re.findall('[a-zA-Z]', string.lower()):
        print('表达式错误，包涵非法字符！')
        check_result = False
    return check_result
