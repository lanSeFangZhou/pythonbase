def main():
    persons = [True] * 30
    counter = 0
    index = 0
    number = 0
    while counter < 15:
        if persons[index]:
            numer += 1
            if number == 9:
                persons[index] = False
                number = 0
                counter += 1
        index += 1
        index %= len(persons)
    for person in persons:
        print('基' if person else '非', end='')
    print()