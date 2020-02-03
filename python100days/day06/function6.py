# 作用域问题

# 局部作用域
def fool():
    a = 5

fool()
#print(a)

#全局作用域
b = 10

def foo2():
    print(b)

foo2()


def foo3():
    # 局部变量
    c = 100
    print(c)

foo3()
#print(c)


def foo4():
    # 全局变量
    global d
    d = 200
    print(d)

foo4()
print(d)