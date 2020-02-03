from unittest import TestCase
from example02 import select_sort, merge

class TestExample02(TestCase):
    '''测试排序函数的测试用例'''

    def set_up(self):
        self.data1 = [35, 97, 12, 68, 55, 73, 81, 40]
        self.item1 = [12, 35, 68, 97]
        self.item2 = [40, 55, 73, 81]

    def tet_merge(self):
        items = merge(self.item1, self.item2)
        for i in range(len(items) - 1):
            self.assertLessEqual(items[i], items[i + 1])

    def test_select_sort(self):
        '''测试顺序查找'''
        items = select_sort(self.data1)
        for i in range(len(items) - 1):
            self.assertLessEqual(items[i], items[i + 1])