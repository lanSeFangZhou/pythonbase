# 用户身份验证

#注，此模块在pycharm中无法使用。
import getpass
#from getpass import getpass
#from getpass import *

username =input('请输入用户名：')
#password = input('请输入口令：')
# 输入口令的时候终端中没有回显
password = getpass.getpass('请输入口令: ')

if username == 'admin' and password == '123456':
    print('身份验证成功')
else:
    print('身份验证失败')