# -*- coding=utf-8 -*-
# Python 3.6

from tabulate import tabulate
import numpy as np

# 不同类型的数据，list和dict和numpy还有pandas数据
list_data = [["Sun", 696000, 1989100000],
             ["Earth", 6371, 5973.6],
             ["Moon", 1737, 73.5],
             ["Mars", 3390, 641.85]]
dict_data1 = [{"name": "lin", "age": 22},
              {"name": "yao", "age": 22}]
dict_data2 = {
    "name": ["lin", "yao"],
    "age": [22, 21]
}
# table = np.array([["lin", "yao"],
#                   [22, 22]]).T

# # 自行加入头文件
# print(tabulate(list_data, headers=["Planet", "R (km)",
#                                "mass (x 10^29 kg)"]))
# # 如果headers="firstrow"，则会使用第一行的内容作为表头
# print(tabulate([["Name", "Age"], ["Alice", 24],
#                 ["Bob", 19]], headers="firstrow"))
# print(tabulate(list_data, headers="firstrow"))
# print(tabulate(dict_data1, headers="keys"))
# print(tabulate(dict_data2, headers="keys"))

# # 显示行号
# print(tabulate(list_data, showindex="always"))

# # 换图表样式
# print(tabulate(dict_data1, headers="keys",
#                showindex="always", tablefmt="grid"))
# print(tabulate(dict_data1, headers="keys",
#                showindex="always", tablefmt="fancy_grid"))
# print(tabulate(dict_data1, headers="keys",
#                showindex="always", tablefmt="grid"))

# # 精确数字到后面几位，精确的位数可以是个list分别精确
# print(tabulate([["pi", 3.141593], ["e", 2.718282]], floatfmt=".4f"))
# print(tabulate([[0.123456, 0.123456, 0.123456]], floatfmt=(".1f", ".3f")))
