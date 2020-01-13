# coding=utf-8
'''
@Description: reduce函数
@Author: superz
@Date: 2020-01-13 14:21:54
@LastEditTime: 2020-01-13 14:35:50
'''
import sys

curr_word = None
curr_count = 0

for line in sys.stdin:
    word, count = line.split("\t")
    count = int(count)
    if curr_word == word:
        curr_count += count
    else:
        if curr_word:
            print("{0}\t{1}".format(curr_word, curr_count))

        curr_word = word
        curr_count = count

if curr_word == word:
    print('{0}\t{1}'.format(curr_word, curr_count))
