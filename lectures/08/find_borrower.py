#!/usr/bin/env python3


from loans import get_borrower

import sys


if __name__ == '__main__':

    try:
        laptop = sys.argv[1]

        print(f'Laptop {laptop} is on loan to {get_borrower(laptop)}.')

    except IndexError:
        print(f'Usage: {sys.argv[0]} <laptop>')
    except KeyError:
        print('Laptop is not on load.')
