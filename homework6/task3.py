#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task3.py
@Time : 2020/04/15 23:07:57
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib

"""
定义一个字典类：dictclass。完成下面的功能：
dict = dictclass({你需要操作的字典对象})
1 删除某个key
del_dict(key)
2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
get_dict(key)
3 返回键组成的列表：返回类型;(list)
get_key()
4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
update_dict({要合并的字典})
"""

class DictClass(object):
    __cls_dict = {}

    def __init__(self, any_dict):
        self.__cls_dict = any_dict

    def del_dict(self, key):
        if key in self.__cls_dict:
            del self.__cls_dict[key]

    def get_dict(self, key):
        if key in self.__cls_dict:
            return self.__cls_dict[key]
        else:
            return "key not found"

    def get_key(self):
        key_list = []
        for k in self.__cls_dict.keys():
            key_list.append(k)
        return key_list

    def update_dict(self, any_dict):
        self.__cls_dict.update(any_dict)
        value_list = []
        for v in self.__cls_dict.values():
            value_list.append(v)
        return value_list

if __name__ == '__main__':
    dict1 = DictClass({'1': 'a', '2': 'b'})
    dict1.del_dict('1')
    print(dict1.get_dict('1'))
    print(dict1.get_dict('2'))
    print(dict1.get_key())
    print(dict1.update_dict({'3': 'c', '4': 'd'}))
