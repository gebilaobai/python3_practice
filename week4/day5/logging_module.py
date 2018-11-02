# -*- coding: utf-8 -*-
# Time    : 2018/11/2 11:21
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : logging_module.py
# Software: PyCharm

"""
python 的logging模块提供了标准的日志接口，可以通过ta存储各种格式的热I之，logging的日志可以分为五个级别
    1.debug()
    2.info()
    3.warning()
    4.error()
    5.critical()

默认情况下python的logging模块将日志大隐刀了标准输出中，且只显示了大于等于warning级别的日志，这说明默认的日志级别设置为
warning（日志级别等级CRITICAL>ERROR>WARNING>INFO>DEBUG>NOTSET）；
默认的日志格式为：
    日志类别：logger名称：用户输出消息
"""

import logging


logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')

# print(''.center(20,'*'))

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)',
                    datefmt ='%a, %d %b %Y %H:%M:%s',
                    filename='/temp/test.log',
                    filemode='w'
                    )
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')