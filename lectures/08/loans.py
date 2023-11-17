#!/usr/bin/env python3

DEFAULT_LOAN_FILE = 'loans.txt'


def read_loans(loan_file=DEFAULT_LOAN_FILE):
    loans = {}

    with open(loan_file, 'r') as lf:
        for line in lf:
            lappy, borrower = line.strip().split(' ')
            loans[lappy] = borrower

    return loans


def write_loans(loans, loan_file=DEFAULT_LOAN_FILE):
    with open(loan_file, 'w') as lf:
        for lappy in loans:
            lf.write(f'{lappy} {loans[lappy]}\n')


def get_borrower(laptop):
    current_loans = read_loans()

    return current_loans[laptop]


def on_loan(laptop):
    current_loans = read_loans()

    return laptop in current_loans.keys()


if __name__ == '__main__':
    print(read_loans())

    loans = read_loans()
    write_loans(loans)
