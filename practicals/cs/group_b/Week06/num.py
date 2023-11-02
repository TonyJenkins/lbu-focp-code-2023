#!/usr/bin/env python3


def num_range(n):

    if len(n) == 0:
        raise ValueError('no range of empty sequence')

    return max(n) - min(n)


if __name__ == '__main__':

    numbers = []

    while True:
        next_num = input("> ")

        if not next_num:
            break
        else:
            try:
                numbers.append(int(next_num))
            except ValueError:
                print('Please enter integers!')

    print(num_range(numbers))
