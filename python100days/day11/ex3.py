'''
异常机制 - 处理程序在运行时可能发生的状态
'''

import time
import sys

filename = input('请输入文件名：')
try:
    with open(filename) as f:
        lines = f.readlines()
except FileNotFoundError as msg:
    print('无法打开文件：', filename)
    print(msg)
else:
    for line in lines:
        print(line.rstrip())
        time.sleep(0.5)
finally:
    # 此处最适合做善后工作
    print('不管发生什么，我都会执行')