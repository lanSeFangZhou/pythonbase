'''
闲聊数据类型

0. 针对视频中小甲鱼提到的小漏洞，再次改进我们的小游戏：当用户输入错误类型的时候，及时提醒用户重新输入，防止程序崩溃。
1. 写一个程序，判断给定年份是否为闰年。（注意：请使用已学过的 BIF 进行灵活运用）
2.请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！
'''

num = input('请输入一个整数:')
if type(num) == 'int':
    print("输入数据类型正确，请输入一个整数！")
else:
    print('输入数据类型错误！')

year = int(input('请输入年份:'))
#if year % 4 == 0 and year % 400 != 0:
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
   print(year + "年是闰年！")
else:
   print(year + '是平年！')

# 学习了type和isInstance

temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
# 这种想法是因为type(1)会返回<class 'int'>,如果type(temp)
#  返回结果一直说明输入是整数。
while type(temp) != type(1):
    print("抱歉，输入不合法,", end='')
    temp = input("请输入一个整数：")

# 也可以这样
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
# not操作符的作用是将布尔类型的结果翻转：即取反的意思，not True == False
while not isinstance(temp, int):
    print("抱歉，输入不合法，", end='')
    temp = input("请输入一个整数：")

# 以上方法的思路是正确的，不过似乎忽略了一点：就是input()的返回值始终是字符串,
# 所以type(temp)永远是<class 'str'>!
# 其实有蛮多的做法可以实现的，不过就目前我们学习过的内容来看，还不足够。
# 所以，在让大家动手完成这道题之前，小甲鱼介绍一些新东西给大家！
# s为字符串
s = ''
s.isalnum() # 所有的字符都是数字或字母，为真返回True，否则返回False
s.isalpha() # 所有的字符都是字母，为真返回True，否则返回False
s.isdigit() # 所有的字符都是数字，为真返回True,否则返回False
s.islower() # 所有的字符都是小写，为真返回True，否则返回False
s.isupper() # 所有的字符都是大写，为真返回True，否则返回False
s.istitle() # 所有的单词都是首字母大写，为真返回True,否则返回False
s.isspace() # 所有的字符都是空白字符，为真返回True,否则返回False
s = 'I Love FishC'
s.isupper()

# 好了，文字教程就到这里，大家赶紧趁热打铁，改造我们的小游戏吧
import random
times = 3
secret = random.randint(1, 10)
print('------------------我爱鱼C工作室------------------')
guess = 0
print("不妨猜一下小甲鱼现在心里想的是哪个数字：", end="")
while (guess != secret) and (times > 0):
    temp = input()
    while not temp.isdigit():
        temp =  input("抱歉，您的输入有误，请输入一个整数：")
    guess = int(temp)
    times = times - 1 #用户每输入一次，可用机会就-1
    if guess == secret:
        print("我草，你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("哥，大了大了。。。")
        else:
            print("嘿，小了小了。。。")
        if times > 0:
            print("再试一次吧：", end=" ")
        else:
            print("机会用光咯T_T")
print('游戏结束，不玩啦^_^')


#能被4整除但不能被100整除，或者能被400整除的都是闰年
# 方案1
temp = input("请输入一个年份：")
while not temp.isdigit():
    temp = input("抱歉，您的输入有误，请输入一个整数：")
year = int(temp)
if year/400 == int(y/400):
    print(temp + '是闰年！')
else:
    if (year/4 == int(year/4)) and (year/100 != int(year/100)):
        print(temp + "是闰年！")
    else:
        print(temp + "不是闰年！")

# 方案2
temp = input("请输入一个年份：")
while not temp.isdigit():
    temp = input('输入不合法，请输入一个整数：')
year = int(temp)
if year == 0:
    print('%d 不是一个闰年！' %year)
else:
    if year%400 == 0:
        print('%d 是一个闰年！' %year)
    else:
        if year%4 == 0 and year%100 != 0:
            print('%d 是一个闰年！' %year)
        else:
            print('%d 不是一个闰年!' %year)