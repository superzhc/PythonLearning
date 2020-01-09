# coding=utf-8
'''
@Description: NumPy操作和创建数值数据
@Author: superz
@Date: 2020-01-10 01:34:26
@LastEditTime : 2020-01-10 01:51:29
'''

import timeit
import numpy as np

if __name__ == "__main__":
    # 测试numpy的性能
    # print(timeit.timeit("[i**2 for i in lst]",
    #                     setup="lst=range(1000)", number=1))
    # print(timeit.timeit(stmt="(np.arange(1000))**2",
    #                     setup="import numpy as np", number=1))

    # 查找东西
    # np.lookfor("create array")

    # 创建数组
    # 手动创建
    a = np.array([0, 1, 2, 3])
    print(a)

    print(a.ndim)
    print(a.shape)
    print(len(a))

    # 创建数组的函数
    a = np.arange(10)  # 均匀分布
    print(a)
    b = np.arange(1, 9, 2)
    print(b)
    c = np.linspace(0, 1, 6)  # 起点、终点、数据点
    print(c)
