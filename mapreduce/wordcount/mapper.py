# coding=utf-8
'''
@Description: map实现
@Author: superz
@Date: 2020-01-13 14:21:47
@LastEditTime: 2020-01-13 14:27:13
'''
import sys

# 从输入流STDIN读取每一行
for line in sys.stdin:
    # 将每一行分隔成一个个单词
    words = line.split()
    # 生成每个单词的计数，如：(superz,1)
    for word in words:
        print("{0}\t{1}".format(word, 1))
