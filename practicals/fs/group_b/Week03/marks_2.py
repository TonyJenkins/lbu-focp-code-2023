#!/usr/bin/env python3


from statistics import mean, stdev


if __name__ == '__main__':

    NUMBER_OF_MARKS = 5

    list_of_marks = []

    for mark in range(NUMBER_OF_MARKS):
        next_mark = int(input('Enter Mark: '))
        list_of_marks.append(next_mark)

    highest = max(list_of_marks)
    lowest = min(list_of_marks)

    average = mean(list_of_marks)
    standard_deviation = stdev(list_of_marks)

    print()
    print(f'Highest Mark: {highest}.')
    print(f'Lowest Mark:  {lowest}.')
    print(f'Average Mark: {average}.')
    print(f'Standard Dev: {standard_deviation}.')

    print()
    print(f'The highest mark was {highest}, the lowest was {lowest}'
          f' and the average as {average}.')
