# 用for循环实现1~100之间的偶数求和

sum = 0
#最后一个参数是步长
for i in range(2, 101, 2):
    sum += i
print(sum)