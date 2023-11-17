#!/usr/bin/env python3


from loans import read_loans


if __name__ == '__main__':

    current_loans = read_loans()

    for lappy in current_loans:
        print(f'{lappy}: Loaned to {current_loans[lappy]}')
