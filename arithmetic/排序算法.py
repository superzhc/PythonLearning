# coding=utf-8
'''
@Description: 排序算法（选择、冒泡和归并）
@Author: superz
@Date: 2020-01-04 21:57:57
@LastEditTime : 2020-01-04 22:18:15
'''


def select_sort(origin_items, comp=lambda x, y: x < y):
    """
    简单选择排序
    """

    items = origin_items[:]
    for i in range(len(items)-1):
        min_index = i
        for j in range(i+1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def bubble_sort(origin_items, comp=lambda x, y: x > y):
    """
    高质量冒泡排序（搅拌排序）
    """
    items = origin_items[:]
    for i in range(len(items)-1):
        swapped = False
        for j in range(i, len(items)-1-i):
            if comp(items[j], items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items)-2-i, i, -1):
                if comp(items[j-1], items[j]):
                    items[j], items[j-1] = items[j-1], items[j]
                    swapped = True
        if not swapped:
            break

    return items


if __name__ == "__main__":
    lst = [3, 2, 4, 1, 6, 5]
    print(select_sort(lst))
    print(bubble_sort(lst))
