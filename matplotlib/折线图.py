# coding=utf-8
'''
@Description: 折线图
@Author: superz
@Date: 2020-01-05 21:58:46
@LastEditTime : 2020-01-05 22:15:27
'''

from pylab import *


def single_chart1():
    t = arange(0.0, 2.0, 0.01)
    s = sin(2.5*pi*t)
    plot(t, s)

    # 设置x轴文本
    xlabel("time(s)")
    # 设置y轴文本
    ylabel("voltage(mV)")
    # 设置图表标题
    title("Sine Wave")
    # 打开网格
    grid(True)
    show()


def single_chart2():
    t = arange(0.0, 20.0, 1)
    s = [x for x in range(20)]
    plot(t, s)

    xlabel("t")
    ylabel("s")
    title("single_chart2")
    grid(True)
    show()


def multi_chart():
    """多个图"""
    t = arange(0.0, 20.0, 1)
    s1 = [x for x in range(20)]
    s2 = [x for x in range(21)][1:]
    s3 = [x for x in range(22)][2:]
    plot(t, s1)
    plot(t, s2)
    plot(t, s3)

    xlabel("t")
    ylabel("s")
    title("single_chart2")
    grid(True)
    show()


if __name__ == "__main__":
    # single_chart2()
    multi_chart()
