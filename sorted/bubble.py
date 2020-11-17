# -*- coding: utf-8 -*-
# @Time: 2020/11/17 16:13
# @Author: Mr.Cheng
# @Site : 
# @File: bubble.py
# @Software: PyCharm py3.7


def start(args):
    """冒泡"""
    for i in range(0, len(args)+1):
        for j in range(1, len(args)-i):
            if args[j-1] > args[j]:
                args[j],args[j-1] = args[j-1],args[j]
    return args


li = [11,22,55,77,99,88,44,33,66]
print(start(li))


