# -*- coding: utf-8 -*-
# Time    : 2018/10/19 15:49
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : 3 menu 高大上版.py
# Software: PyCharm

menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

current_layer = menu
parent_layer = menu
while True:
    for k in current_layer:
        print(k)
    choice = input('>>>:').strip()
    if len(choice) == 0:
        continue
    if choice in current_layer:
        parent_layer = current_layer
        current_layer = current_layer[choice]
    elif choice == 'b':
        current_layer = parent_layer

    else:
        print('无此项，请重新输入。。。')


