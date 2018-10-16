# -*- coding: utf-8 -*-
# Time    : 2018/9/30 0:51
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : shoppingcar.py
# Software: PyCharm

"""
1、输入自己所拥有的余额
2、展示商品列表和对应的单价
3、输入想要购买的商品编号
4、判断余额是否够支付所选商品
5、余额不足时提示并重新显示商品列表
6、余额充足时，商品进入购入车，并在余额中扣除商品金额，询问是否继续购买
7、不继续购买时退出购物
"""

product_list = [
    ('Macbook', 9000),
    ('Book', 88),
    ('bike', 500),
    ('kindle', 599),
    ('Mi8', 3299),
    ('MiTV', 2099),
    ('tesla', 900000)
]

cart = []

saving = input('请输入您的金额：')

if saving.isdigit():
    saving = int(saving)
    while True:
        for i, v in enumerate(product_list, 1):
            print(i, '—', v)
        choice = input('请选择您想要购买商品的编号【退出请输入q】：')
        if choice.isdigit():
            choice = int(choice)
            if 0 < choice <= len(product_list):
                p_item = product_list[choice - 1]
                price = p_item[1]
                if price <= saving:
                    saving = saving - price
                    cart.append(p_item)
                else:
                    print("您的余额不足~！，还剩%s" % saving)
            else:
                print('您输入的编码商品不存在')
        elif choice == 'q':
            print ('------------您已经购买如下商品---------------')
            for i in cart:
                print (i)
            print ("您的余额为%s元" % saving)
            break
        else:
            print ("请输入正确的商品编号")
