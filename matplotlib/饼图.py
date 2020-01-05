# coding=utf-8
'''
@Description: 饼图示例
@Author: superz
@Date: 2020-01-05 23:52:09
@LastEditTime : 2020-01-06 00:00:56
'''

if __name__ == "__main__":
    from matplotlib import pyplot

    labels = ["Python", "C++", "Java", "Scala"]
    sizes = [215, 130, 210, 90]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0, 0)

    # pyplot.pie(sizes, explode=explode, labels=labels, colors=colors,
    #            autopct="%1.1f%%", shadow=True, startangle=140)

    # 要添加图例，使用pyplot.legend()函数
    patches, texts = pyplot.pie(
        sizes, colors=colors, shadow=True, startangle=90)
    pyplot.legend(patches, labels, loc="best")

    pyplot.axis("equal")
    pyplot.show()
