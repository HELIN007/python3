# -*- coding=utf-8 -*-
# Python 3.6

import matplotlib.pyplot as plt
import jieba
from jieba.analyse import extract_tags
import random
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image


def make_img(image):
    """
    将照片二值化，能够使得轮廓更清楚
    """
    im = Image.open(image).convert('L')  # 转化为黑白图片
    threshold = 140  # 阈值
    table = [1 if i < threshold else 0 for i in range(256)]
    # table = []
    # for i in range(256):
    #     if i < threshold:
    #         table.append(0)
    #     else:
    #         table.append(1)
    im = im.point(table, '1')
    im.save('ciyuntu_test.jpg')
    # im.transpose(Image.ROTATE_270).save('ciyuntu_test.jpg')  # 有时候需要旋转
    return im


def make_cloud_by_all_text():
    text = open('shijiuda.txt', 'r').read()
    # 结巴分词:cut_all参数可选, True为全模式，False为精确模式,默认精确模式
    cut_text = jieba.cut(text)
    # 必须给个符号分隔开分词结果,否则不能绘制词云
    result = "/".join(cut_text)
    im = Image.open('ciyuntu_test.jpg')
    graph = np.array(im)
    # 指定中文字体路径，如果mask为空的话，width和height就会发挥作用
    wc = WordCloud(font_path=r'/System/Library/Fonts/PingFang.ttc',
                    background_color='black', width=200, height=200, mask=graph,
                    max_font_size=300, max_words=1000).generate(result)
    wc.recolor(colormap=plt.get_cmap('rainbow'))
    # # 两种转换颜色的方式
    # wc.recolor(color_func=grey_color_func)
    # # 绘制文字的颜色以背景图颜色为参考
    # image_color = ImageColorGenerator(graph)  # 从背景图片生成颜色值，但二值图不行
    # wc.recolor(color_func=image_color)
    wc.to_file('全词云图.jpg')  # 保存图片
    plt.figure('全词云图')
    plt.imshow(wc)
    plt.axis('off')
    plt.show()


def make_cloud_by_frequency(im):
    text = open('shijiuda.txt', 'r').read()
    # 结巴分词:cut_all参数可选, True为全模式，False为精确模式,默认精确模式
    cut_text = jieba.cut(text)
    # 必须给个符号分隔开分词结果,否则不能绘制词云
    result = "/".join(cut_text)
    # topK是指频率最高的前几个词
    tags = extract_tags(sentence=result, topK=100)
    words = [word for word in jieba.cut(result, cut_all=True)]
    # 存成字典形式{单词：频率}
    word_freq = {}
    for tag in tags:
        freq = words.count(tag)
        word_freq[tag] = freq
    # # 按照频率排序，准备画图的
    # usewords = sorted(word_freq.items(), key=lambda item: item[1])
    # print(usewords)
    # freqs = np.array(usewords).T
    # print(freqs)
    graph = np.array(im) * 255  # bool值转化为数值
    # # 这样也可以，这样的话就不需要传入值了，但是需要之前保存过照片
    # im = Image.open('ciyuntu_test.jpg')
    # graph = np.array(im)
    # 得是字典形式
    wc = WordCloud(font_path=r'/System/Library/Fonts/PingFang.ttc',
                    background_color='black', width=1000, height=1000, mask=graph,
                    max_font_size=200, max_words=1000).generate_from_frequencies(word_freq)
    wc.recolor(colormap=plt.get_cmap('rainbow'))
    # wc.to_file('高频词云图.jpg')
    plt.figure('高频词云图')
    plt.imshow(wc)
    # plt.axis('off')
    plt.show()


def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    # 调成自己喜欢的颜色
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)


def main():
    image = 'test.png'
    im = make_img(image)
    # # 传入值，不需要读取保存的照片
    # make_cloud_by_frequency(im)
    # 不传入值，读取保存的照片
    make_cloud_by_all_text()

if __name__ == '__main__':
    main()
