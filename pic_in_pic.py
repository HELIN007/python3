# -*- coding=utf-8 -*-
# Python 3.6

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib import ticker

font = FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

# 理解成画布
fig = plt.figure(figsize=(8, 5))

# 创建数据
x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([1, 3, 4, 2, 5, 8, 6])

# 科学计数法
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1, 1))

# 理解成占画布的百分比
# 设figure的大小是10x10，
# 那这组数据就表示是在由(1, 1)开始，宽8，高8的坐标系内
left, buttom, width, height = 0.1, 0.1, 0.8, 0.8

# 理解成画布中的子图1，在这里是大图
ax1 = fig.add_axes([left, buttom, width, height], facecolor='y')
ax1.plot(x, y**2, 'b', linewidth=2)
ax1.plot([x[5], x[5]], [0, y[5]**2], linestyle=':', color='m')
ax1.set_ylabel('面积 $(m^2)$', FontProperties=font, color='b', fontsize=20)
for label in ax1.get_yticklabels():
    label.set_color("b")
ax1.set_xlim(0, 10)
ax1.set_ylim(0, np.max(y)**2)
ax1.xaxis.labelpad = 1  # 轴上的标签和轴上的数字的间距
ax1.yaxis.labelpad = 1
ax1.yaxis.set_major_formatter(formatter)  # 科学计数法
ax1.set_title('主图', FontProperties=font, fontsize=15, color='r')
plt.setp(ax1.get_yticklabels(), rotation=30, horizontalalignment='right')
plt.setp(ax1.get_xticklabels(), rotation=30, horizontalalignment='right')
# # 双坐标轴
# ax1_1 = ax1.twinx()
# ax1_1.set_ylabel('体积 $(m^3)$', FontProperties=font, color='r', fontsize=20)
# ax1_1.plot(x, y**3, 'r', linewidth=2)
# for label in ax1_1.get_yticklabels():
#     label.set_color("r")
# ax1_2 = ax1.twiny()
# ax1_2.set_xlabel('第二个x轴', FontProperties=font, color='c', fontsize=20)
# for label in ax1_2.get_xticklabels():
#     label.set_color("c")
# 改变坐标轴的属性
ax1.spines['bottom'].set_color('r')
ax1.spines['left'].set_color('b')
ax1.spines['left'].set_linewidth(2)
ax1.spines['bottom'].set_linewidth(2)
# ax1.spines['top'].set_color('none')  # 隐藏坐标轴
ax1.spines['top'].set_visible(False)


# 理解成子图2，大图中的小图
left, buttom, width, height = 0.2, 0.6, 0.2, 0.2
ax2 = fig.add_axes([left, buttom, width, height])
ax2.plot(x**2, y, 'y-', linewidth=2)
ax2.xaxis.set_major_formatter(formatter)
ax2.minorticks_on()  # 开启小刻度
# 主刻度朝里，可以调为out和inout，也可以调为minor和both
ax2.tick_params(which='major', direction='in')
ax2.tick_params(which='minor', width=2, length=5)  # 调整刻度的粗细长短
# 哪个轴显示刻度及刻度值
ax2.tick_params(top='on', bottom='off', left='off', right='off')
ax2.tick_params(labeltop='on', labelbottom='on',
                labelleft='off', labelright='off')
# ax2.set_xticks(range(9))  # ax2.set_xticks([])  # 去掉刻度
ax2.grid(color='m', alpha=0.5, linestyle='-.', linewidth=0.5)  # 网格线
ax2.set_title('子图1', FontProperties=font, fontsize=5, color='b')

# 理解成子图3，大图中的小图
left, buttom, width, height = 0.65, 0.2, 0.2, 0.2
ax3 = fig.add_axes([left, buttom, width, height])
ax3.plot(x, y, 'g', linewidth=2)
# 更换坐标轴的起点
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)
ax3.spines['left'].set_position(('data', 2))
ax3.spines['bottom'].set_position(('data', 5))
ax3.annotate('测试点', xy=(2, 5), xytext=(3, 6), FontProperties=font,
             arrowprops=dict(arrowstyle="fancy",
                             fc='r',
                             ec='1',
                             connectionstyle="arc3,rad=1"))


plt.show()
