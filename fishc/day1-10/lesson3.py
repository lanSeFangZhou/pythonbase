'''
0. 还记得我们第一讲的动动手的题目吗？这一次要求使用变量，计算一年有多少秒？

提示：可以以 DaysPerYear（每年天数），HoursPerDay（每天小时数），MinutesPerHour（每小时分钟数），SecondsPerMinute（每分钟秒数）为变量名。


1. 关于最后提到的长字符串（三重引号字符串）其实在 Python3 还可以这么写，不妨试试，然后比较下哪种更方便？

>>> string = (
"我爱鱼C，\n"
"正如我爱小甲鱼，\n"
"他那呱唧呱唧的声音，\n"
"总缠绕于我的脑海，\n"
"久久不肯散去……\n")
复制代码


2. 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！
'''

DaysPerYear = 365
HoursPerDay = 24
MinutesPerHour = 60
SecondsPerMinute = 60
sumSecond = DaysPerYear * HoursPerDay * MinutesPerHour * SecondsPerMinute
#TODO  为什么不能打印
#print("一年总共的秒数是：" + sumSecond)

string = '''
我爱鱼C
正如我爱小甲鱼
他那呱唧呱唧的声音
总缠绕于我的脑海
久久不肯散去……
'''

# 字符串的段落输入，避免拼接错误

