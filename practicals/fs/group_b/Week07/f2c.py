#!/usr/bin/env python3


import sys


def f2c(f):
    return (f - 32) * (5 / 9)


if __name__ == '__main__':

    try:
        if sys.argv[1].endswith('F'):
            temp_f = float(sys.argv[1][:-1])

            print(f'{f2c(temp_f):.2f}C')
        else:
            print('Error in input value')

    except IndexError:
        print('Missing temperature!')
    except ValueError:
        print('Error in input value')
