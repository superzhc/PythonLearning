# coding=utf-8
'''
@Description: 查找算法
@Author: superz
@Date: 2020-01-04 22:21:50
@LastEditTime : 2020-01-04 23:11:21
'''

from math import log2, factorial
from matplotlib import pyplot
import numpy


def seq_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1


def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items)-1
    while start <= end:
        mid = (start+end)//2
        if key > items[mid]:
            start = mid+1
        elif key < items[mid]:
            end = mid-1
        else:
            return mid
    return -1


if __name__ == "__main__":
    # lst = [1, 2, 3, 4, 5, 6]
    # print(seq_search(lst, 3))
    # print(bin_search(lst, 3))

    num = 6
    style = ["r-.", "g-*", "b-o", "y-x", "c-^", "m-+", "k-d"]
    legends = ["对数", "线性", "线性对数", "平方", "立方", "几何级数", "阶乘"]
    x_data = [x for x in range(1, num)]
    y_data1 = [log2(y) for y in range(1, num)]
    y_data2 = [y for y in range(1, num)]
    y_data3 = [y*log2(y) for y in range(1, num)]
    y_data4 = [y**2 for y in range(1, num)]
    y_data5 = [y**3 for y in range(1, num)]
    y_data6 = [3**y for y in range(1, num)]
    y_data7 = [factorial(y) for y in range(1, num)]
    y_datas = [y_data1, y_data2, y_data3, y_data4, y_data5, y_data6, y_data7]
    for index, y_data in enumerate(y_datas):
        pyplot.plot(x_data, y_data, style[index])
    pyplot.legend(legends)
    pyplot.xticks(numpy.arange(1, 6, step=1))
    pyplot.yticks(numpy.arange(0, 260, step=15))
    pyplot.show()
