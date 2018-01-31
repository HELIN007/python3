# -*- coding=utf-8 -*-
# Python 3.6

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def draw_picture(vegetables, model):
    v_name = [name[0] for name in vegetables]  # 字典读取key
    zh_price = np.array([price[1][1] for price in vegetables])  # 读取第一列数据
    jp_price = np.array([price[1][0] for price in vegetables])  # 读取第二列数据
    price_mean = jp_price / zh_price  # 求平均值

    plt.style.use('classic')
    # 可以多配置默认设置plt.rcParams
    # plt.rcParams.update({'figure.autolayout': True})
    plt.rcParams['figure.autolayout'] = True
    # plt.rcParams['figure.dpi'] = 150  # 更改默认显示dpi
    # plt.rcParams['savefig.dpi'] = 1000  # 更改默认存储dpi
    plt.rcParams['ytick.direction'] = 'inout'  # 设置坐标轴上的刻度是否突出，'in'、'out'、'inout'。

    font = FontProperties(fname='/System/Library/Fonts/PingFang.ttc')
    fig, ax = plt.subplots(figsize=(8, 4))

    # 个人发现，感觉plt和ax.set_是一个用法，能互换
    if model:
        ax.set_title('中日野菜の値段対比', FontProperties=font, fontsize=20)
        plt.xlabel('値段(円/kg)', FontProperties=font)
        # plt.ylabel('野菜種類', FontProperties=font)
        ax.set_yticks(range(14))  # 效果和plt.yticks()一样
        ax.set_yticklabels(v_name, FontProperties=font, rotation=10)
        # # 和上面两句效果一样
        # plt.yticks(range(14), v_name, FontProperties=font, rotation=10)
        bar_positions = np.arange(14)
        # 如果是水平画图的话，条形的宽度此时就是height，默认0.8
        ax.barh(bar_positions, jp_price, alpha=0.3, height=0.8, align='center', color='b')
        ax.barh(bar_positions, zh_price, alpha=1, align='center', color='r')

        for i, (x, y) in enumerate(zip(jp_price, bar_positions)):
            plt.text(x, y, '%d' % x, fontsize=10)
            plt.text(x + 150, y, '约%d倍' %
                    price_mean[i], fontsize=10, color='r', FontProperties=font)

        for x, y in zip(zh_price, bar_positions):
            plt.text(x + 20, y, '%d' % x, fontsize=10)

        plt.xlim(0, 2900)
        plt.legend(['日本', '中国'], loc='upper right', fontsize=10, prop=font)
        # fig.savefig('1.png')
        plt.show()
    else:
        x = np.arange(14)
        # plt.xlim(-0.5, 13.5)  # 限制横坐标轴的范围
        # plt.ylim(0, 3000)  # 限制纵坐标轴的范围
        plt.axis([-0.5, 13.5, 0, 2500])  # 一步到位[xmin,xmax,ymin,ymax]
        # bar的横坐标，纵坐标，宽度，是否居中（默认从x起），颜色，透明度
        # 如果是垂直画图的话，条形的宽度此时就是weight，默认0.8，edgecolor条形边的颜色，linewidth条形边的宽度
        plt.bar(x, jp_price, width=0.8, align='center', color='g', alpha=0.8, edgecolor='r', linewidth=2)
        plt.bar(x, zh_price, width=0.4, align='center', color='r', alpha=1)

        # 对应坐标，填写相应文本，图片显示乱码的话加上字体路径
        plt.xticks(x, v_name, size='small', rotation=30, fontproperties=font, color='r')
        # plt.yticks(np.arange(0, 2500, 200))  # 设置刻度步长
        plt.xlabel('野菜', fontproperties=font)
        plt.ylabel('値段', fontproperties=font)

        # 图例是有顺序的，按画的先后顺序，loc=0自行找位置，ncol是要显示的函数，frameon=False是去掉框框
        # loc='best', 'upper right', 'center', 'lower left', 'lower right'
        plt.legend(['日本', '中国'], loc=0, ncol=2, fontsize=10, prop=font, frameon=False)
        # plt.grid()  # 加网格线
        plt.show()


def main():
    vegetables = {
        'キャベツ': [384, 9],
        '白ねぎ': [842, 19],
        '青ねぎ': [2482, 69],
        '白菜': [331, 6],
        'ほうれん草': [1491, 34],
        'レタス': [1254, 26],
        '玉ねぎ': [213, 16],
        'きゅうり': [730, 40],
        'トマト': [778, 30],
        'なす': [850, 44],
        'ピーマン': [1151, 30],
        '大根': [321, 12],
        '人参': [347, 13],
        '馬鈴薯': [282, 13]
    }
    # 按第一列数据从大到小排序，默认reverse为false即从小到大
    vegetables = sorted(vegetables.items(),
                        key=lambda item: item[1][0], reverse=True)
    draw_picture(vegetables, model=1)


if __name__ == '__main__':
    main()
