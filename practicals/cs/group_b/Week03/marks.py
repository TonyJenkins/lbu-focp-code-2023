#!/usr/bin/env python3

if __name__ == '__main__':

    mark_1 = int(input('Enter Mark #1 '))
    mark_2 = int(input('Enter Mark #2 '))
    mark_3 = int(input('Enter Mark #3 '))
    mark_4 = int(input('Enter Mark #4 '))
    mark_5 = int(input('Enter Mark #5 '))

    highest = max(mark_1, mark_2, mark_3, mark_4, mark_5)
    lowest = min(mark_1, mark_2, mark_3, mark_4, mark_5)
    average = (mark_1 + mark_2 + mark_3 + mark_4 + mark_5) / 5.0

    print()
    print(f'Highest Mark: {highest}')
    print(f'Lowest Mark:  {lowest}')
    print(f'Average Mark: {average}')
