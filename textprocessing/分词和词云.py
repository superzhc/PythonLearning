# coding=utf-8
'''
@Description: 分词和词云
@Author: superz
@Date: 2020-01-07 00:28:25
@LastEditTime : 2020-01-07 01:34:34
'''

import jieba
from jieba import posseg, analyse
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np


def test_seg():
    # text = "这是一个测试的信息"
    text = "天龙八部的主角有乔峰和阿朱"
    words = jieba.cut(text, cut_all=False)
    print(f"精确模式：{'/'.join(words)}")

    words = jieba.cut(text, cut_all=True)
    print(f"全模式：{'/'.join(words)}")

    words = jieba.cut_for_search(text)
    print(f"搜索引擎模式：{'/'.join(words)}")


def test_pseg():
    text = "天龙八部的主角有乔峰和阿朱"
    words = posseg.cut(text)
    for word, flag in words:
        print(f"{word} {flag}")


if __name__ == "__main__":
    # 读取人名
    # with open("./data/天龙八部人名.txt", "r", encoding="utf-8") as f:
    #     for line in f.readlines():
    #         if line:
    #             # print(line)
    #             # 添加自定义的词
    #             jieba.add_word(line)

    # 通过词典文件
    # jieba.load_userdict("./data/天龙八部人名.txt")

    # 读取天龙八部的资源
    with open("./data/天龙八部.txt", "r", encoding="utf-8") as f:
        text = f.read()

    # test_seg()
    # test_pseg()

    # 主题词提取
    # TF-IDF算法
    result = analyse.extract_tags(
        text, topK=50, withWeight=True, allowPOS=())  # nr词性为人名，识别的有点问题，待深入研究 todo
    # print("got keywords:", len(result), type(result))

    # TextRank算法
    # result = analyse.textrank(text, topK=50)
    # print(result)

    # 词云
    img = Image.open("./data/python-logo.jpg")
    print(img.size)
    img = img.resize((600, 600), Image.ANTIALIAS)
    mask = np.array(img)
    wc = WordCloud(font_path=r"C:\Windows\Fonts\simfang.ttf",
                   background_color="white",
                   mask=mask, contour_width=2, contour_color="steelblue")
    md = dict()
    for key, value in result:
        md[key] = value
    wc.generate_from_frequencies(md)
    wc.to_file("./data/z-wordcloud.png")

    image_colors = ImageColorGenerator(mask)
    wc.recolor(color_func=image_colors)
    wc.to_file("./data/z-image_colors.png")
