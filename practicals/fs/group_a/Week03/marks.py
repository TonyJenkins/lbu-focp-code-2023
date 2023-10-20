#!/usr/bin/env python3

if __name__ == '__main__':
    mark_1 = int(input('Enter mark #1: '))
    mark_2 = int(input('Enter mark #2: '))
    mark_3 = int(input('Enter mark #3: '))
    mark_4 = int(input('Enter mark #4: '))
    mark_5 = int(input('Enter mark #5: '))

    max_mark = max(mark_1, mark_2, mark_3, mark_4, mark_5)
    min_mark = min(mark_1, mark_2, mark_3, mark_4, mark_5)
    avg_mark = (mark_1 + mark_2 + mark_3 + mark_4 + mark_5)/5

    print(f'Highest Mark: {max_mark}')
    print(f'Lowest Mark:  {min_mark}')
    print(f'Average Mark: {avg_mark:.2f}')