#!/usr/bin/env python3

import sys


if __name__ == '__main__':

    try:

        num_1 = int(sys.argv[1])
        num_2 = int(sys.argv[2])

        print(num_1 + num_2)

    except (IndexError, ValueError,):
        print(f'{sys.argv[0]}: Wrong CLAs')
