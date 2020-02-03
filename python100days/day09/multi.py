'''
多重继承
- 通过多重继承可以给一个类的对象具备多方面的能力
- 这样在设计类的时候可以避免设计太多层次的复杂的继承关系
'''

class Father(object):

    def _init_(self, name):
        self._name = name

    def gamble(self):
        print('%s在打麻将.' % self._name)

    def eat(self):
        print('%s在大吃大喝.' % self._name)

class Monk(object):

    def _init_(self, name):
        self._name = name

    def eat(self):
        print('%s在细嚼慢咽.' % self._name)

    def play_piano(self):
        print('%s在弹钢琴.' % self._name)

# 试一试下面的代码看有什么区别
# class Son(Monk, Father, Musician)：
# class Son(Musician, Father, Monk)：

class Son(Father, Monk, Musician):

    def _init_(self, name):
        Father._init_(self, name)
        Monk._init_(self, name)
        Musician._init_(self, name)

son = Son('王宝强')
son.gamble()
# 调用继承自Father的eat方法
son.eat()
son.chant()
son.play_piano()