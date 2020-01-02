# coding=utf-8
'''
@Description: 字符串相关操作示例
@Author: superz
@Date: 2020-01-03 00:40:47
@LastEditTime : 2020-01-03 00:49:46
'''


def reverse_str1(str):
    '''
    反转字符串
    '''
    return ''.join(reversed(str))


def reverse_str2(str):
    '''
    反转字符串
    '''
    return str[::-1]


print(reverse_str1("superz"))
print(reverse_str2("superz"))
