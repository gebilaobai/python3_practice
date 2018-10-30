# -*- coding: utf-8 -*-
# Time    : 2018/10/30 23:30
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : sys_module.py
# Software: PyCharm

"""
sys模块在跟python解释器交互
"""

import sys

# sys.argv  命令行参数List，第一个元素是程序本身路径，后面可以跟若干自定义参数从而实现不同的功能
# def post():
#     print('post ok')
#
#
# def download():
#     print('download ok')
#
#
# if sys.argv[1] == 'post':
#     post()
# elif sys.argv[1] == 'download':
#     download()

# sys.exit()  # 退出程序，正常退出时exit(0)

sys.version  # 获取python解释器的版本

print(sys.path)  # 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值

print(sys.platform)  # 返回操作系统平台名称

