# -*- coding: utf-8 -*-
# Time    : 2018/10/30 0:42
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : yield伪并发.py
# Software: PyCharm

# 还可以通过yield是现在单线程的情况下实现并发运算的效果

import time


def consumer(name):
    print('%s 准备吃包子啦！' % name)
    while True:
        baozi = yield

        print('包子[%s]来了，被[%s]吃了' % (baozi, name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print('%s开始准备做包子啦！' % name)
    for i in range(10):
        time.sleep(1)
        print('做了2个包子！')
        c.send(i)
        c2.send(i)


producer('NeoBY')