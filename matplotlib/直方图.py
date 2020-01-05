# coding=utf-8
'''
@Description: 直方图
@Author: superz
@Date: 2020-01-05 22:17:22
@LastEditTime : 2020-01-05 23:35:54
'''

import numpy as np
from matplotlib import pyplot, mlab

if __name__ == "__main__":
    # x = [21, 22, 23, 4, 5, 6, 77, 8, 9, 10, 31,
    #      32, 33, 34, 35, 36, 37, 18, 49, 50, 100]
    # num_bins = 5

    # 测试数据
    mu = 100
    sigma = 15
    x = mu+sigma*np.random.randn(10000)

    num_bins = 20

    # 数据的直方图
    n, bins, patches = pyplot.hist(
        x, num_bins, normed=1, facecolor="blue", alpha=0.5)

    # add a 'best fit' line
    y = mlab.normpdf(bins, mu, sigma)
    pyplot.plot(bins, y, "r--")
    pyplot.xlabel("Smarts")
    pyplot.ylabel("Probability")
    pyplot.title(r"Histogram of IQ: $\mu=100$, $\sigma=15$")
    # Tweak spacing to prevent clipping of ylabel
    pyplot.subplots_adjust(left=0.15)
    pyplot.show()
