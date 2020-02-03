'''
函数的参数
- 位置参数
- 可变参数
- 关键字参数
- 命名关键字参数
'''

#参数默认值
def f1(a, b=5, c=10):
    return a + b * 2 + c * 3

print(f1(1, 2, 3))
print(f1(100, 200))
print(f1(100))
print(f1(c=2, b=2, a=1))

#可变参数
def f2(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(f2(1, 2, 3))
print(f2(1, 2, 3, 4, 5))
print(f2())

# 关键字参数
def f3(**kw):
    if 'name' in kw:
        print('欢迎您%s!' % kw['name'])
    elif 'tel' in kw:
        print('你的联系电话是: %s' % kw['tel'])
    else:
        print('没找到你的个人信息！')

param = {'name': 'mike', 'age': 28}
f3(**param)
f3(name='mike', age=28, tel='123456789')
f3(user='mike', age=28, tel='123456789')
f3(user='mike', age=28, mobile='123456789')