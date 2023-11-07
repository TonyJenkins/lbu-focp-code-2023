#!/usr/bin/env python3


import sys


if __name__ == '__main__':
    # print(sys.argv)
    try:
        print(f'Hello, {sys.argv[1]}!')
    except IndexError:
        print('Hello, World!')
