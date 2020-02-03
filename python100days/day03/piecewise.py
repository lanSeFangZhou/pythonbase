'''
分段函数求值
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
'''

x = int(input('请输入X的值：'))
if x > 1:
    value = 3 * x -5
elif x > -1:
    value = x + 2
else:
    value = 5 * x + 3
print('%d 对应的函数值是：' %x, value)