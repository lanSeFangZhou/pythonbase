'''
0. 设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含"*"则不计算在内。

1. 编写一个程序，求 100~999 之间的所有水仙花数。
如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数。

2. 三色球问题
有红、黄、绿三种颜色的求，其中红球 3 个，黄球 3 个，绿球 6 个。先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配。
  不知道

3.请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！
  range()

'''

'''
origin = '123456'
count = 3
while True:
    pwd = input('请输入密码：')
    if origin == pwd:
        print('密码输入成功')
    else:
        if pwd.__contains__('*'):
            print('密码输入错误')
            continue
        else:
            count -= 1
            if count <= 0:
                print('密码输入错误超过三次，账户被锁定！')
                break


num = 100
while num < 1000:
    if (num / 100 * num / 100 + num / 10 * num / 10 + num % 100 * num % 100) == num:
        print("水仙花数是:" + str(num))
'''

for red in range(1, 4):
    for yellow in range(1, 4):
        for green in range(1,9):
            print(str(red) + str(yellow) + str(green))

count = 3
password = 'FishC.com'
while count:
    passwd = input('请输入密码：')
    if passwd == password:
        print('密码正确，进入程序......')
        break
    elif '*' in passwd:
        print('密码不能含有"*"号！您还有', count, '次机会！', end=' ')
        continue
    else:
        print('密码输入错误！您还有', count - 1, '次机会！', end=' ')
    count -= 1

for i in range(100, 1000):
    sum = 0
    temp = i
    while temp:
        sum = sum + (temp%10) ** 3
        temp //= 10 #注意这里要是用地板除哦~
    if sum == i:
        print(i)

# range(2,7)是产生[2,3,4,5,6]5个数，绿球不能是1个，以为如果绿球是1个的话，
# 红球+黄球需要有7个才能符合题意，而红球和黄球每种只有3个，因此是range(2,7)
print('red\tyellow\tgreen')
for red in range(0, 4):
    for yellow in range(0, 4):
        for green in range(2, 7):
            if red + yellow + green == 8:
                # 注意，下边不是字符串拼接，因此不用‘+’哦
                print(red, '\t', yellow, '\t', green)