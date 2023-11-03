#!/usr/bin/env python3

import sys


if __name__ == '__main__':

    try:

        table = int(sys.argv[1])

        if 0 <= table <= 12:
            for line in range(13):
                print(f'{line} x {table} = {line * table}')
        else:
            print(f'{sys.argv[0]}: Value out of range')

    except (IndexError, ValueError,):
        print(f'{sys.argv[0]}: Wrong CLAs')
