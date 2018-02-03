# -*- coding=utf-8 -*-
# Python 3.6

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib import ticker

font = FontProperties(fname='/System/Library/Fonts/PingFang.ttc')


def main_pic(fig, x, y):
    # 理解成占画布的百分比
    # 设figure的大小是10x10，
    # 那这组数据就表示是在由(1, 1)开始，宽8，高8的坐标系内
    left, buttom, width, height = 0.1, 0.1, 0.8, 0.8
    # 理解成画布中的子图1，在这里是主图
    ax = fig.add_axes([left, buttom, width, height], facecolor='y')
    ax.plot(x, y**2, 'b', linewidth=2)  # 在子图里画图
    ax.plot([x[5], x[5]], [0, y[5]**2], linestyle=':', color='m')  # 画虚线
    ax.set_ylabel('面积 $(m^2)$', FontProperties=font, color='b', fontsize=20)  # 设置y轴内容
    # 改变y轴属性，如这里改变颜色
    for label in ax.get_yticklabels():
        label.set_color("b")
    # 设置坐标轴的范围
    ax.set_xlim(0, 10)
    ax.set_ylim(0, np.max(y)**2)
    # 轴上的标签和轴上的数字的间距
    ax.xaxis.labelpad = 1
    ax.yaxis.labelpad = 1
    ax.set_title('主图', FontProperties=font, fontsize=15, color='r')  # 设置标题
    # 设置轴上的属性，倾斜30°
    plt.setp(ax.get_yticklabels(), rotation=30, horizontalalignment='right')
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
    # 改变坐标轴的属性
    ax.spines['bottom'].set_color('r')
    ax.spines['left'].set_color('b')
    ax.spines['left'].set_linewidth(2)  # 坐标轴的粗细
    ax.spines['bottom'].set_linewidth(2)
    # ax.spines['top'].set_color('none')  # 隐藏坐标轴
    ax.spines['top'].set_visible(False)
    is_scientific_notation(ax, 1, 1)
    is_twin_axis(ax, 1, 1)


def is_twin_axis(ax, x, y):
    # 双坐标轴
    # x轴共用
    if x:
        ax = ax.twinx()
        ax.set_ylabel('体积 $(m^3)$', FontProperties=font, color='r', fontsize=20)
        ax.plot(x, y**3, 'r', linewidth=2)
        for label in ax.get_yticklabels():
            label.set_color("r")
    # y轴共用
    if y:
        ax = ax.twiny()
        ax.set_xlabel('第二个x轴', FontProperties=font, color='c', fontsize=20)
        for label in ax.get_xticklabels():
            label.set_color("c")


def is_scientific_notation(ax, x, y):
    # 科学计数法
    formatter = ticker.ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((-1, 1))
    # x轴用科学计数法
    if x:
        ax.xaxis.set_major_formatter(formatter)
    # y轴用科学计数法
    if y:
        ax.yaxis.set_major_formatter(formatter)
    return ax


def picture_1(fig, x, y):
    # 理解成子图2，大图中的小图
    left, buttom, width, height = 0.2, 0.6, 0.2, 0.2
    ax = fig.add_axes([left, buttom, width, height])
    ax.plot(x**2, y, 'y-', linewidth=2)
    is_scientific_notation(ax, 1, 0)
    ax.minorticks_on()  # 开启小刻度
    # 主刻度朝里，可以调为out和inout，也可以调为minor和both
    ax.tick_params(which='major', direction='in')
    ax.tick_params(which='minor', width=2, length=5)  # 调整刻度的粗细长短
    # 哪个轴显示刻度及刻度值
    ax.tick_params(top='on', bottom='off', left='off', right='off')
    ax.tick_params(labeltop='on', labelbottom='on',
                    labelleft='off', labelright='off')
    # ax.set_xticks(range(9))  # ax.set_xticks([])  # 去掉刻度
    ax.grid(color='m', alpha=0.5, linestyle='-.', linewidth=0.5)  # 网格线
    ax.set_title('子图1', FontProperties=font, fontsize=5, color='b')


def picture_2(fig, x, y):
    # 理解成子图3，大图中的小图
    left, buttom, width, height = 0.65, 0.2, 0.2, 0.2
    ax = fig.add_axes([left, buttom, width, height])
    ax.plot(x, y, 'g', linewidth=2)
    # 更换坐标轴的起点
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_position(('data', 2))
    ax.spines['bottom'].set_position(('data', 5))
    # 给某点加注释，要注释的点是xy，注释内容的位置在xytext
    ax.annotate('测试点', xy=(2, 5), xytext=(3, 6), FontProperties=font,
                arrowprops=dict(arrowstyle="->",  # 箭头类型
                                fc='r',  # 箭头颜色
                                ec='0',  # 箭头边的颜色
                                connectionstyle="arc3,rad=1"))  # 设置弯的箭头


def main():
    # 创建数据
    x = np.array([1, 2, 3, 4, 5, 6, 7])
    y = np.array([1, 3, 4, 2, 5, 8, 6])
    # 理解成画布
    fig = plt.figure(figsize=(10, 5))
    main_pic(fig, x, y)
    picture_1(fig, x, y)
    picture_2(fig, x, y)
    plt.show()

if __name__ == '__main__':
    main()
