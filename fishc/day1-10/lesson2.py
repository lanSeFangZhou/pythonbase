'''
0. 编写程序：hello.py，要求用户输入姓名并打印“你好，姓名！”

例如：



1. 编写程序：calc.py 要求用户输入1到100之间数字并判断，输入符合要求打印“你妹好漂亮”，不符合要求则打印“你大爷好丑”

例如：

2. 如果非要在原始字符串结尾输入反斜杠，可以如何灵活处理？

2. 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！
'''

name = input("请输入您的姓名:")
print('你好,' + name)

num = int(input("请输入1到100间的数字:"))
#if num >= 1 & num <=100:
if 1 <= num <= 100:
    print("你妹好漂亮！")
else:
    print('你大爷好丑T_T')

while True:
    if not num.isdigit():
        print('输入不合法，请重新输入数字：', end='')
        num = input()
    else:
        num = int(num)
        if num > 100:
            print('你大爷好丑')
        else:
            print('你妹好漂亮')
        break
# 还是不熟练

str = r'C:\Program Files\FishC\Good''\\'