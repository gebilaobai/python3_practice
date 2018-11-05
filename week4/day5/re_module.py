# -*- coding: utf-8 -*-
# Time    : 2018/11/5 15:09
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : re_module.py
# Software: PyCharm

"""
简介：
    就其本质而言，正则表达式（或RE）是一种小型的、高度专业化的变成语言，（在python中）它内嵌在python中，并通过re模块实现
正则表达式模块被编译成一系列的字节码，然后由用C编写的匹配引擎执行。

正则表达式是用来做什么的？
    1、用来匹配字符串的；

string提供的方法是完全匹配
引入正则的目的：完成模糊匹配

元字符：. ^ $ * + ? { } [ ] | ( ) \
    【.】:代指一位任意字符
"""

import re



# ret = re.findall('w\w{2}l','hello world')
# print(ret)

#全部匹配
# ret = re.findall('alex','asdfasdfasdfalexadfasdfasdfasdfalex')
# print(ret)  # ['alex', 'alex']

# .通配符
ret = re.findall('w..l','hello world') # .只能代指任意一个字符
print(ret)

# ^尖角符
ret = re.findall('^h...o','good hello world') # ^只对字符串的开始进行匹配
print(ret)

# $ 从结尾匹配
ret = re.findall('a..x$','asdfasdfasdfalex') # $只对字符串的结尾进行匹配
print(ret)

# * 重复匹配它的范围是[0,+∞]
ret = re.findall('a.*li','fddfsalexlidfasdfasd') # *表示重复前面的多次（不区分元字符和普通字符）
print(ret)


# + 重复匹配它的范围是[1,+∞]
ret = re.findall('ab+','kjldfabbbbbbbbh') # +表示重复前面的多次（不区分元字符和普通字符）
print(ret)

ret = re.findall('a+b','aaaabdfdfdfaabdfdfdfab') # +表示重复前面的多次（不区分元字符和普通字符）
print(ret)

# ? [0,1]
ret = re.findall('a?b','aaaabdfdfdfaabdfdfdfabbbb') # a?b 表示0~1个a
print(ret)

# {}指定重复次数进行匹配,大括号里面可以加范围

ret = re.findall('a{1,3}b','babsaabsaaabsaaaab')  # 通过{}指定重复次数进行匹配
print(ret)

"""
结论：
* 等于 {0,+∞}
+ 等价于{1,+∞}
? 等价于{0,1}
"""

# [] 字符集
ret = re.findall('a[c,d]x','acxvvvvadx')  #
print(ret)

ret = re.findall('[a-z]','acxvvvvadx')  #
print(ret)

# []字符集：可以取消元字符的特殊功能(\ ^ - 三个元字符例外)
ret = re.findall('[w,*,.,]','awdx.,')
print(ret)

ret = re.findall('[1-9a-zA-Z]','12tyAS')
print(ret)
ret = re.findall('[1-9，a-z，A-Z]','12tyAS')
print(ret)

# ^放在[]中表示取反
ret = re.findall('[^t]','12tyAS')
print(ret)


"""
\ ：
    1、反斜杠后边跟元字符去除特殊功能；
    2、反斜杠后边跟普通字符实现特功能；
    
\d 匹配任何十进制数；它相当于类[0-9]
\D 匹配任何非数字字符；它相当于类[^0-9]
\s 匹配任何空白字符；它相当于类[\t\n\r\f\v]
\S 匹配任何非空白字符；它相当于类[^\t\n\r\f\v]
\w 匹配任何字母数字字符；它相当于类[a-zA-Z0-9]
\W 匹配任何非字母数字字符；它相当于类[^a-zA-Z0-9]
\b: 匹配一个特殊字符边界，也就是指单词和空格间的位置
"""
ret = re.findall('\d','12tyAS')
print(ret)

ret = re.findall('\D','12tyAS')
print(ret)

ret = re.findall('\sasd','fak asd')
print(ret)
ret = re.findall('\Sasd','fakasd')
print(ret)

ret = re.findall('\w','fak asd')
print(ret)

ret = re.findall('\W','  12tyAS  ')
print(ret)

ret = re.findall(r'I\b','hello,I am a LI$ST.')
print(ret)

#######################################################################
# 匹配出满足条件的第一个结果
ret = re.search('sb','fjalskdjfslkdfjsblskdfjsb')
print(ret)
print(ret.group())