#!/usr/bin/env python3

from loans import read_loans, write_loans, on_loan

import sys


if __name__ == '__main__':

    try:
        new_lappy = sys.argv[1]
        new_borrower = sys.argv[2]

        if on_loan(new_lappy):
            print(f'Error: Laptop {new_lappy} is already on loan.')
        else:
            current_loans = read_loans()
            current_loans[new_lappy] = new_borrower

            write_loans(current_loans)

    except IndexError:
        print(f'Usage: {sys.argv[0]} <laptop> <student>')
