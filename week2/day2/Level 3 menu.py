# -*- coding: utf-8 -*-
# Time    : 2018/10/17 0:13
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : Level 3 menu.py
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
# 精简的写法，十分推荐需要仔细琢磨
# exit_flag = False
# current_layer = menu
# layers = [menu]
# while not exit_flag:
#     for k in current_layer:
#         print(k)
#     choice = input('>>:').strip()
#     if choice == 'b':
#         current_layer = layers[-1]
#         layers.pop()
#     elif choice not in current_layer:
#         continue
#     else:
#         layers.append(current_layer)
#         current_layer = current_layer[choice]


# 非常low的写法，大量的重复代码

back_flag = False
exit_flag = False
while not back_flag and not exit_flag:
    for k in menu:
        print(k)
    choice = input("1>>:").strip()
    if choice == 'q':
        exit_flag = True
    if choice in menu:
        while not back_flag and not exit_flag:  # 让程序停留在第二层
            for k2 in menu[choice]:
                print(k2)
            choice2 = input("2>>:").strip()
            if choice2 == 'b':
                back_flag = True
            if choice2 == 'q':
                exit_flag = True
            if choice2 in menu[choice]:
                while not back_flag and not exit_flag:
                    for k3 in menu[choice][choice2]:
                        print(k3)
                    choice3 = input("3>>:").strip()
                    if choice3 == 'b':
                        back_flag = True
                    if choice3 == 'q':
                        exit_flag = True
                    if choice3 in menu[choice][choice2]:
                        while not back_flag and not exit_flag:
                            for k4 in menu[choice][choice2][choice3]:
                                print(k4)
                            choice4 = input("4>>:").strip()
                            print("已到最后一层")
                            if choice4 == 'b':
                                back_flag = True
                            if choice4 == 'q':
                                exit_flag = True

                        else:
                            back_flag = False

                else:
                    back_flag = False

        else:
            back_flag = False



