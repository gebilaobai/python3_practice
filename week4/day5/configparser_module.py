# -*- coding: utf-8 -*-
# Time    : 2018/11/5 14:21
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : configparser_module.py
# Software: PyCharm

"""
configparser模块
    用于生成和修改常见配置文档，当前模块的名称在python3.x版本中变更为configparser
"""

import configparser
config = configparser.ConfigParser()


#用于生成
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9'
#                      }
#
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'
# topsecret['ForwardX11'] = 'no'
# config['DEFAULT']['ForwardX11'] = 'yes'
#
# with open('example.ini','w') as configfile:
#     config.write(configfile)


# 读取配置信息
# config.read('example.ini')
# print(config.sections())
# print(config.defaults())
#
# print('bitbucket.org' in config.sections())
# print(config['bitbucket.org']['User'])

# for key in config['bitbucket.org']:
#     print(key)

# 删配置内容

# config.read('example.ini')
# config.remove_section('topsecret.server.com')
# config.write(open('example.ini', 'w'))

# 改配置内容
config.read('example.ini')
config.set('bitbucket.org','User','NeoBY')
config.write(open('example.ini', 'w'))