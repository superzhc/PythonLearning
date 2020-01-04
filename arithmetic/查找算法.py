# coding=utf-8
'''
@Description: 查找算法
@Author: superz
@Date: 2020-01-04 22:21:50
@LastEditTime : 2020-01-04 22:30:03
'''


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
    lst = [1, 2, 3, 4, 5, 6]
    print(seq_search(lst, 3))
    print(bin_search(lst, 3))
