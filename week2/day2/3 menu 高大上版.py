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

current_layer = menu  # 实现动态循环
parent_layers = []  # 保存所有父级，最后一个元素永远都是父级

while True:
    for k in current_layer:
        print(k)
    choice = input('>>>:').strip()
    if len(choice) == 0:
        continue
    if choice in current_layer:
        parent_layers.append(current_layer)  # 在进入下一层之前，把当前层也就是下一层的父级追加到列表中，下一次loop，当用户选择b的时候就可以直接取列表的最后一个值出来
        current_layer = current_layer[choice]  # 当前层改成子层
    elif choice == 'b':
        if parent_layers:
            current_layer = parent_layers.pop()     # 取出列表的最后一个值，因为他是当前层的父级
    else:
        print('无此项，请重新输入。。。')
