# -*- coding: utf-8 -*-
# Time    : 2018/10/30 20:53
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : os_module.py
# Software: PyCharm

import os

print(os.getcwd())  # 获取当前工作目录

# os.chdir('d:\\') # 改变当前脚本工作目录；相当于shell下的cd
print(os.getcwd())

print(os.curdir)  # 返回当前目录：.
print(os.pardir)  # 获取当前目录的父目录字符串名：..

# os.makedirs('abc\\neoby\\baiy')  # 在当前所在目录中创建目录，可生成多层递归目录
# os.removedirs('abc\\neoby\\baiy')  # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除
#
# os.mkdir('dirname')  # 生成单级目录；相当于shell中mkdir dirname
# os.rmdir('dirname')  # 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中的rmdir dirname

print(os.listdir('c:/'))  # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式存储

# os.remove('文件名')  # 删除一个文件，只能删除文件，不能删除文件夹
# os.rename('oldname', 'newname')  # 重命名文件或目录

"""
获取文件/目录信息对象
# os.stat_result(st_mode=33206, st_ino=5348024557505284, st_dev=2522775020, st_nlink=1, st_uid=0, st_gid=0, st_size=1195, st_atime=1540907681, st_mtime=1540907681, st_ctime=1540904006)
"""
print(os.stat('os_module.py'))

print(os.sep)  # 输出当前操作系统特定的路径分隔符，win下为\\，linux下为/  使用技巧把os.sep做为一个变量，采用格式化输出的方式加入路径中
print(os.linesep)  # 输出当前平台使用的行终止符，win下为\r\n，linux下为\n
print(os.pathsep)  # 输出用于分隔文件路径的字符串
print(os.name)  # 输出字符串指示当前使用的平台；，win下为nt;linux下为posix

print(os.system('dir'))  # 执行shell命令，直接显示

print(os.environ)  # 获取系统环境变量

print(os.path.abspath('./os.module.py'))


print(os.path.split('./os.module.py'))  # 将 path分割成目录和文件名二元组返回

print(os.path.dirname('E:\python3_practice\week4\day5\os.module.py')) # 返回path的目录。其实就是os.path.split(path)的第一个元素

print(os.path.basename('E:\python3_practice\week4\day5'))  # 返回path最后的文件名，如果path以/或\结尾，那么久会返回空值。

print(os.path.exists('./abc'))  # 判断path是否存在，存在返回True；不存在返回False
print(os.path.isabs('c:\\'))  # 判断path是否是绝对路径，如果是返回True，不是返回False

print(os.path.isfile('E:\python3_practice\week4\day5\os.module.py'))  # 判断path是否是一个存在的文件，是返回True，不是返回False
print(os.path.isdir('E:\python3_practice\week4\day5'))  # 判断path是否是一个存在的目录，是返回True，不是返回False


# 路径拼接
# os.path.join([path1,path2])

# os.path.getatime('filename') # 返回path所指向的文件或者目录的最后存储时间
# os.path.getmtime('filename') # 返回path所指向的文件或者目录的最后修改时间
