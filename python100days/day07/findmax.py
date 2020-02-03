# 找出列表中最大或最小的元素

def main():
    fruits = ['grade', 'apple', 'strawberry', 'waxberry', 'pitaya']
    # 直接使用内置的max函数和min函数找出列表中最大和最小元素
    print(max(fruits))
    print(min(fruits))
    max_value = min_value = fruits[0]
    for index in range(1, len(fruits)):
        if fruits[index] > max_value:
            max_value = fruits[index]
        elif fruits[index] < min_value:
            min_value = fruits[index]
    print('Max:', max_value)
    print('Min:', min_value)
# 想一想如果最大的元素有两个要找出第二大的又该怎么做


if __name__ == '__main__':
    main()