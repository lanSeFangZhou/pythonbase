# 输入半径计算圆的周长和面积

import math

radius =float(input("请输入圆的半径："))
len = math.pi * 2 * radius
area = math.pi * radius ** 2
print('半径为%.2f的圆的面积为：%.2f' % (radius, area))
print('半径为%.2f的圆的周长为：%.2f' % (radius, len))