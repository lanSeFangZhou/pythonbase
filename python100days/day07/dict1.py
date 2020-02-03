# 定义和使用字典

def main():
    scores = {'aa':95, 'bb': 88, 'cc': 76}
    print(scores['aa'])
    print(scores['bb'])
    for elm in scores:
        print('%s\t---->\t%d' % (elm, scores[elm]))
    scores['bb'] = 65
    scores['dd'] = 59
    scores.update(ee=32, ff=12)
    print(scores)
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))
    print(scores.get('武则天', 60))
    print(scores.popitem())
    print(scores.pop('aa', 100))
    scores.clear()
    print(scores)

if __name__ == '__main__':
    main()