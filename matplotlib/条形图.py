# coding=utf-8
'''
@Description: 条形图示例
@Author: superz
@Date: 2020-01-05 23:38:34
@LastEditTime : 2020-01-05 23:51:41
'''

if __name__ == "__main__":

    import numpy as np
    from matplotlib import pyplot

    objects = {"Python", "C++", "Java", "Perl", "Scala", "Lisp"}
    y_pos = np.arange(len(objects))
    performance = [10, 8, 6, 4, 2, 1]

    # pyplot.bar(y_pos, performance, align="center", alpha=0.5)
    # pyplot.xticks(y_pos, objects)
    # 图表水平创建
    pyplot.barh(y_pos, performance, align="center", alpha=0.5)
    pyplot.yticks(y_pos, objects)
    
    pyplot.ylabel("Usage")
    pyplot.title("Programming language usage")

    pyplot.show()
