# -*- coding: utf-8 -*-
# Time    : 2018/11/8 0:40
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : json_test.py
# Software: PyCharm

import json

dic = {'name':'alex','age':'31'}
data = json.dumps(dic)

f = open('JSON_text','w')
f.write(data)
f.close()

# 也可以使用.dump方法来实现
data = json.dump(dic,f)
