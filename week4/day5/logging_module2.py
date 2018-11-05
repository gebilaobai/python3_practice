# -*- coding: utf-8 -*-
# Time    : 2018/11/5 10:31
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : logging_module2.py
# Software: PyCharm

"""
还有一个模块级别的函数是logging.getLogger([name])返回一个logger对象，如果没有指定名字将返回root logger
"""

import logging

logger = logging.getLogger()
# 创建一个handler用于写入日志文件
fh = logging.FileHandler('test.log')

# 再创建一个handler用于输出到控制台
ch = logging.StreamHandler()

formatter = logging.basicConfig(filename='test.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d',
                    filemode='a')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')