# -*- coding: utf-8 -*-
# Time    : 2018/11/12 16:28
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : XML_module.py
# Software: PyCharm

"""
xml是实现不同语言或程序之间进行数据交换的协议，跟json差不多，但json使用起来更简单，不过，古时候，在json还没诞生的黑暗年
代，大家只能选择用xml呀，至今很多传统公司如金融行业的很多系统的接口还主要是xml。
xml的格式如下，就是通过<>节点来区别数据结构的:
"""

# 查看xml中的内容
# import xml.etree.ElementTree as ET
#
# tree = ET.parse('xml_test')
# root = tree.getroot()
# print(root.tag)
#
# # 遍历xml文档
# for child in root:
#     print(child.tag, child.attrib)
#     for i in child:
#         print(i.tag, i.text)
#
# # 只遍历year节点
# for node in root.iter('year'):
#     print(node.tag, node.text)


# 修改xml中的内容
# import xml.etree.ElementTree as ET
#
# tree = ET.parse('xml_test')
# root = tree.getroot()
#
# for node in root.iter('year'):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#     node.set('updated','yes')
#
# tree.write('xml_test')

# 删除xml内容
# 例如，删除排名超过50的
# import xml.etree.ElementTree as ET
#
# tree = ET.parse('xml_test')
# root = tree.getroot()
#
# for country in root.findall('country'):
#     rank = int(country.find('rank').text)
#     if rank > 50:
#         root.remove(country)
# tree.write('output.xml')

# 创建xml
import xml.etree.ElementTree as ET

new_xml = ET.Element('namelist')
name = ET.SubElement(new_xml, 'name', attrib={'enrolled': 'yes'})
age = ET.SubElement(name, 'age', attrib={'checked':'no'})
sex = ET.SubElement(name, 'sex')
age.text = '33'

name2 = ET.SubElement(new_xml, 'name', attrib={'enrolled':'no'})
age = ET.SubElement(name2,'age')
age.text = '19'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write('creatXML.xml', encoding='utf-8', xml_declaration=True)

ET.dump(new_xml) # 打印生成的格式