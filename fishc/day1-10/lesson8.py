'''
0. 视频中小甲鱼使用 if elif else 在大多数情况下效率要比全部使用 if 要高，但根据一般的统计规律，一个班的成绩一般服从正态分布，
也就是说平均成绩一般集中在 70~80 分之间，因此根据统计规律，我们还可以改进下程序以提高效率。

题目备忘：按照100分制，90分以上成绩为A，80到90为B，60到80为C，60以下为D，写一个程序，当用户输入分数，自动转换为ABCD的形式打印。

1. Python 的作者在很长一段时间不肯加入三元操作符就是怕跟C语言一样搞出国际乱码大赛，蛋疼的复杂度让初学者望而生畏，不过，
如果你一旦搞清楚了三元操作符的使用技巧，或许一些比较复杂的问题反而迎刃而解。
x, y, z = 6, 5, 4
if x < y:
    small = x
    if z < small:
        small = z
elif y < z:
    small = y
else:
    small = z

2.请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！
'''

score = int(input('请输入分数：'))
if score > 90:
    print(str(score) + '对应的等级是A')
elif score > 80:
    print(str(score) + '对应的等级是B')
elif score > 60:
    print(str(score) + '对应的等级是C')
else:
    print(str(score) + '对应的等级是D')

# 不会

# 三元操作符

score = int(input('请输入一个分数：'))
if 80 > score >= 60:
    print('C')
elif 90 > score >= 80:
    print('B')
elif 60 > score >=0:
    print('D')
elif 100 >= score >= 90:
    print('A')
else:
    print('输入错误！')

#small = x if (x < y and x < z) else (y if y < z else z)