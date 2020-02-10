'''
常用操作符

0. 请写一个程序打印出 0~100 所有的奇数。

1. 我们说过现在的 Python 可以计算很大很大的数据，但是......真正的大数据计算可是要靠刚刚的硬件滴，
不妨写一个小代码，让你的计算机为之崩溃？

2. 爱因斯坦曾出过这样一道有趣的数学题：有一个长阶梯，若每步上2阶，最后剩1阶；若每步上3阶，最后剩2阶；
若每步上5阶，最后剩4阶；若每步上6阶，最后剩5阶；只有每步上7阶，最后刚好一阶也不剩。

3.请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！
'''

num = 100
while num > 0:
    if (num % 2 != 0):
        print(num)
    num-=1

'''a = 10000
while True:
    print(a * a * a)
    a +=a'''

range = 1
count = 0
while range > 0:
    if range % 2 == 1 and range % 3 == 2 and range % 5 == 4 \
        and range % 6 == 5 and range % 7 == 0:
        print("台阶总数为：" + str(range))
        count += 1
    if count == 100:
        break
    range += 1

# 运算符的优先级和使用

i = 0
while i < 100:
    if i != 0:
        print(i, end='')
        i += 1
    else:
        i += 1

print(2 ** 2 ** 32)
# 一般很多机子都会在一会儿之后：Memory Overflow,内存不够用
# 涉及到幂操作，结果都是惊人的。


x = 7
i = 1
flag = 0
while i <= 100:
    if (x%2 == 1) and (x%3 == 2) and (x%5 == 4) and (x%6 == 5):
        flag = 1
    else:
        x = 7 * (i + 1) #根据题意，x一定是7的整数倍，所以每次乘以7
    i += 1
if flag == 1:
    print('阶梯数是：', x)
else:
    print('在程序限定的范围内找不到答案！')