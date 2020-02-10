'''
多个线程共享数据 - 没有锁的情况
'''

from time import sleep
from threading import Thread, Lock

class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁才能执行后续的代码
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 这段代码放在finally中保证释放锁的操作一定要执行
            self._lock.release()

    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._accout = account
        self._money = money

    def run(self):
        self._accout.deposit(self._money)

def main():
    account = Account()
    threads = []
    # 创建100个存款的线程向同一个账户中存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等所有的存款的线程都执行完毕了
    for t in threads:
        t.join()
    print('账户余额为：Y%d元' % account.balance)

if __name__ == '__main__':
    main()