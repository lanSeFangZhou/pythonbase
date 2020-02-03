'''
写入csv文件
'''

import csv

class Teacher(object):

    def __init__(self, name, age, title):
        self._name = name
        self._age = age
        self._title = title
        self._index = -1

    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @property
    def title(self):
        return self._title

filename = 'teacher.csv'
teachers = [Teacher('骆驼', 38, '龟龟'), Teacher('哈哈', 12, '专家')]

try:
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for teacher in teachers:
            writer.writerow([teacher.name, teacher.age, teacher.title])
except BaseException as e:
    print('无法写入文件:', filename)
else:
    print('保存数据完成！')