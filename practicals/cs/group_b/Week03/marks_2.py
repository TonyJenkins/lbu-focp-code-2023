#!/usr/bin/env python3


from statistics import mean


if __name__ == '__main__':

    NUMBER_OF_MARKS = 6

    marks = []

    for counter in range(NUMBER_OF_MARKS):
        mark = int(input('Enter Next Mark '))
        marks.append(mark)

    highest = max(marks)
    lowest = min(marks)
    average = mean(marks)

    print()
    print(f'Highest Mark: {highest}')
    print(f'Lowest Mark:  {lowest}')
    print(f'Average Mark: {average}')
