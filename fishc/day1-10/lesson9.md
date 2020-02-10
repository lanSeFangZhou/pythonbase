#了不起的分支和循环3

0. 下面的循环会打印多少次"I Love FishC"？  
for i in range(0, 10, 2):  
    print('I Love FishC')  
    5次，步长为2  
    5次，因为从0开始，到10结束，步长为2。

1. 下面的循环会打印多少次"I Love FishC"？
for i in 5:
print('I Love FishC')
    5次  
    会报错，上节课的课后习题我们提到了in是"成员资格运算符",而不是像C语言那样去使用  
    for语法。python的for更像脚本语言的foreach。

2. 回顾一下 break 和 continue 在循环中起到的作用？  
   break结束循环  
   continue跳出当前这轮循环，继续下一轮循环
   break语句的作用是终止当前循环，跳出循环体。  
   continue语句的作用是终止本轮循环并开始下一轮循环(这里要注意的是:在开始下一轮循环  
   之前,会先测试循环条件)。

3. 请谈下你对列表的理解？
   列表，就类似于java中的数组，有下标  
   嗯，有些知识点需要自己总结才能加固，下节课小甲鱼将跟大家畅谈一个打了激素的数组:列表,  
   不容错过哦...

4. 请问 range(10) 生成哪些数？
   1-9之间的数字  
   会生成range(0, 10),list(range(0, 10))转换成列表是：[0, 1, 2, 3, 4, 5, 6, 7,  
    8, 9],注意不包含10哦。

5. 目测以下程序会打印什么？  
   while True:  
    while True:  
        break  
        print(1)  
    print(2)  
    break  
print(3)  
    23  
    会打印2(换行)3
    
6. 什么情况下我们要使循环永远为真？
   while True:
   无限循环时
   不明确循环的次数，比如用户输入密码时  
   同样用于游戏实现，因为只要游戏运行着，就需要时刻接收用户输入，因此使用永远为真确保  
   游戏在线。操作系统也是同样的道理，时刻待命，操作系统永远为真的这个循环叫做消息循环。  
   另外，很多通讯服务器的客户端/服务器系统也是通过这样的原理来工作的。

7. 【学会提高代码的效率】你的觉得以下代码效率方面怎样？  
有没有办法可以大幅度改进(仍然使用while)？  
i = 0  
string = 'ILoveFishC.com'  
while i < len(string)):  
    print(i)  
    i += 1  
    
有

print('ILoveFishC.com' * ('ILoveFishC.com'.length() - 1))  
这段代码之所以"效率比较低",是因为每次循环都需要调用一次len()函数(我们还没有学到函数  
使得概念,小甲鱼这里为零基础的朋友形象的解释下：就像你打游戏打的正HIGH的时候，老妈让  
你去买盐......你有两种选择，一次买一包，一天去买五次，或者一次性买5包回来，老妈要就  
直接给他。)
```
i = 0
string = 'ILoveFishC.com'
length = len(string)
while i < length:
  print(i)
  i += 1
```
***
# 课后笔记
1. while循环语句：
```
while 条件:
    循环体
```
2. for循环语句
```python
for 目标 in 表达式:
    循环体
```
3. range()函数：range([start], stop[,step=1]),有三个参数，中括号中的内容可选，  
step是步进，这个BIF的作用是生成一个从start参数的值开始到stop参数的值结束的数字  
序列，经常与for循环联合使用。记住，是左闭右开区间！
4. break:跳出循环体
5. continue:终止本轮循环，并开始下一轮循环(如果下一轮循环的条件为真)
```python
for i in range(10):
    if i % 2 != 0:
        print(i)
        continue
    i += 2
    print(i)
```     
    