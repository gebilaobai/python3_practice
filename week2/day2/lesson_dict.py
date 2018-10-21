# -*- coding: utf-8 -*-
# Time    : 2018/10/16 23:16
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : lesson_dict.py
# Software: PyCharm


"""
不可变的数据类型：整型，字符串，元组
可变的数据类型：列表，字典
参考资料：www.cnglogs.com/yuanchenqi/articles/5782764.html

字典的两大特点：1、无序；2、键唯一
"""

# dic = {'name':'neoby', 'age':31, 'hobby':{'girl_name':'铁锤', 'age':32}, 'is_handsome':True}
#
#
# print(dic['hobby'])

# 字典的操作：单一修改，key不存在的话做新增操作，key存在的话做修改操作
# dic1 = {'name':'neoby'}
# dic1['age']=18
# print(dic1)
#
# #方法setdefault，key存在，不改动，返回字典中相应的key对应的value
# #key不存在，在字典中新增新的键值对，返回新增的key对应的value
# dic1.setdefault('age', 34)
# print(dic1)
# dic1.setdefault('hobby','girl')
# print(dic1)

# # 查 通过key去查找
# dic3 = {'name': 'neoby', 'age': 18, 'hobby': 'girl'}
# print(dic3['name'])
# print(dic3.keys())
# print(type(dic3.keys()))
# print(type(list(dic3.keys())))
# print(dic3.values())
# print(type(dic3.values()))
# print(type(list(dic3.values())))
# print(dic3.items())
# print(type(dic3.items()))
# print(type(list(dic3.items())))


# # 改 通过key 修改 value
# dic3 = {'name': 'neoby', 'age': 18, 'hobby': 'girl'}
# dic3['name']= 'baiyangbbyy'
# print(dic3)
# # 通过update修改,如果key有重复的进行value覆盖，没有重复的进行追加
# dic4 = {'sex':'male','like':'eat','hobby':'boy'}
# dic3.update(dic4)
# print(dic3)
# print(dic4)


# 删 del指定key，删除对应的key和value；clear清空指定的字典;pop删除字典中指定的键值对，并返回该键值对的值
# dic3 = {'name': 'neoby', 'age': 18, 'hobby': 'girl'}
# del dic3['name']
# print(dic3)
#
# a = dic3.pop('age')
# print(a)
# print(dic3)
#
# dic3.clear()
# print(dic3)
#
# del dic3 # 删除整个字典

# 其他操作以及涉及到的方法
# fromkeys
# dic6=dict.fromkeys(['host1','host2','host3'],'test')
# print(dic6) # {'host1': 'test', 'host2': 'test', 'host3': 'test'}
#
# dic7=dict.fromkeys(['host1','host2','host3'],['test1','test2'])
# print(dic7)

# 字典嵌套

# av_catalog = {
#     "欧美":{
#         "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
#         "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
#         "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
#         "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
#     },
#     "日韩":{
#         "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
#     },
#     "大陆":{
#         "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
#     }
# }
# av_catalog['欧美']['www.youporn.com'][1]='木哈哈'
# print(av_catalog)

# 字典排序 字典没有内置sor方法，只能使用sorted进行排序
# dic={5:'555',2:'666',4:'444'}
# print(sorted(dic,reverse=True))
# print(sorted(dic.values()))
# print(sorted(dic.items()))

# 字典的遍历
# dic5={'name': 'alex', 'age': 18}
#
# for i in dic5:  #推荐用这种，效率高
#     print(i,dic5[i])
#
# for i,v in dic5.items():    #中间有转换过程，转换需要时间效率较低
#     print(i,v)
