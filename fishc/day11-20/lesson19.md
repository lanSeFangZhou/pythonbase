# 第十九课：函数：我的地盘听我的
0. 下边程序会输入什么？
```python
def next():
    print('我在next()函数里...')
    pre()
def pre():
    print('我在pre()函数里...')
    
next()
```
会输出
我在next()函数里...
我在pre()函数里...

1. 请问以下这个函数有返回值吗？
```python
def hello():
    print('Hello FishC!')
```
没有
2. 请问Python的return语句可以返回多个不同类型的值吗？  
可以
3. 目测以下程序会打印什么内容：
```python
def fun(var):
    var = 1314
    print(var, end='')
var = 520
fun(var)
print(var)
```
1314
520
4. 目测以下程序会打印什么内容？
```python
var = ' Hi '
def fun1():
    global var
    var = ' Baby '
    return fun2(var)
def fun2(var):
    var += 'I love you'
    fun3(var)
    return var
def fun3(var):
    var = ' 小甲鱼 '
print(fun1())
```
小甲鱼