#!/usr/bin/env python3

from loans import read_loans, write_loans, on_loan

import sys


if __name__ == '__main__':

    try:
        lappy = sys.argv[1]

        if not on_loan(lappy):
            print(f'Error: Laptop {lappy} is not on loan.')
        else:
            current_loans = read_loans()
            current_loans.pop(lappy)

            write_loans(current_loans)

    except IndexError:
        print(f'Usage: {sys.argv[0]} <laptop>')
