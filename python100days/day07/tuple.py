# 元组的定义和使用

def main():
    # 定义元组
    t = ('Mike', 19, True, '四川眉山')
    print(t)
    # 获取元组中的元素
    print(t[0])
    print(t[1])
    print(t[2])
    print(t[3])
    # 遍历元组中的值
    for member in t:
        print(member)
    # 重新给元组赋值
    # t[0] = '王大锤'  # TypeError
    # 变量t重新引用了新的元组，原来的元组被垃圾回收
    t = ('王大锤', 10, False, '云娜丽江')
    print(t)
    # 元组和列表的转换
    person = list(t)
    person[0] = '莉夏萍玲珑'
    person[1] = 13
    print(person)
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)
    print(fruits_tuple[1])

if __name__ == '__main__':
    main()