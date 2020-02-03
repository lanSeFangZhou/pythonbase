# 字典的常用操作
def main():
    stu = {'name': 'aa', 'age': 18, 'gender': True}
    print(stu)
    print(stu.keys())
    print(stu.values())
    print(stu.items())
    for elm in stu.items():
        print(elm)
        print(elm[0], elm[1])
    if 'age' in stu:
        stu['age'] = 20
    print(stu)
    stu.setdefault('score', 60)
    print(stu)
    stu['score'] = 100
    print(stu)

if __name__ == '__main__':
    main()