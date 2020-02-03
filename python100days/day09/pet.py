from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):

    def _init_(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass

class Dog(Pet):

    def make_voice(self):
        print('%s:汪汪汪...' %s self._nickname)

class Cat(Pet):

    def make_voice(self):
        print('%s:喵...喵...' %s self._nickname)

def main():
    pets = [Dog('旺财'), Cat('凯迪'), Dog('大黄')]
    for pet in pets:
        pet.make_voice

if __name__ == '__main__':
    main()