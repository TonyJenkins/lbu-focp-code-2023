#!/usr/bin/env python3

import sys


if __name__ == '__main__':

    try:
        f = open(sys.argv[1], 'r')
        print('File found.')
    except FileNotFoundError:
        print('File not found')
    except IndexError:
        print(f'{sys.argv[0]}: Missing CLA')
