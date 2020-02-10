#0.请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！
'''
0. 完善第二个改进要求（为用户提供三次机会尝试，机会用完或者用户猜中答案均退出循环）并改进视频中小甲鱼的代码。
import random
times = 3
secret = random.randint(1,10)
print('------------------我爱鱼C工作室------------------')
# 这里先给guess赋值（赋一个绝对不等于secret的值）
guess = 0
# print()默认是打印完字符串会自动添加一个换行符，end=" "参数告诉print()用空格代替换行
# 嗯，小甲鱼觉得富有创意的你应该会尝试用 end="JJ"？
print("不妨猜一下小甲鱼现在心里想的是哪个数字：", end=" ")
while (guess != secret) and (times > 0):
    temp = input()
    guess = int(temp)
    times = times - 1 # 用户每输入一次，可用机会就-1
    if guess == secret:
        print("我草，你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("嘿，小了，小了~~~")
        if times > 0:
            print("再试一次吧：", end=" ")
        else:
            print("机会用光咯T_T")
print("游戏结束，不玩啦^_^")

1. 尝试写代码实现以下截图功能：
需要这样输出：

请输入一个整数:5
1
2
3
4
5
代码如下：

temp = input('请输入一个整数:')
number = int(temp)
i = 1
while number:
    print(i)
    i = i + 1
    number = number - 1
需要打印这样的图案：


请输入一个整数:5
    *****
   ****
  ***
 **
*

2.请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！

'''

import random
times = 3
secret = random.randint(1,10)
print('------------------我爱鱼C工作室------------------')
# 这里先给guess赋值（赋一个绝对不等于secret的值）
guess = 0
# print()默认是打印完字符串会自动添加一个换行符，end=" "参数告诉print()用空格代替换行
# 嗯，小甲鱼觉得富有创意的你应该会尝试用 end="JJ"？
print("不妨猜一下小甲鱼现在心里想的是哪个数字：", end=" ")
while (guess != secret) and (times > 0):
    temp = input()
    guess = int(temp)
    times = times - 1 # 用户每输入一次，可用机会就-1
    if guess == secret:
        print("我草，你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
        break
    else:
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("嘿，小了，小了~~~")
        if times > 0:
            print("再试一次吧：", end=" ")
        else:
            print("机会用光咯T_T")
            break
print("游戏结束，不玩啦^_^")

num = int(input("请输入一个正整数:"))
while num > 0:
    print(num)
    num-=1

num = int(input("请输入一个正整数:"))
while num > 0:
    print(' ' * num, '*' * num)
    num-=1

# 学历了while循环
temp = input("请输入一个整数：")
number = int(temp)
i = 1
while number:
    print(i)
    i = i + 1
    number = number - 1

temp = input("请输入一个整数：")
number = int(temp)
while number:
    i = number - 1
    while i:
        print(' ', end='')
        i = i - 1
    j = number
    while j:
        print('*', end='')
        j = j - 1
    print()
    number = number - 1

num = int(input("请输入一个整数："))
while num:
    print(' ' * (num - 1) + '*'*num)
    num -= 1

