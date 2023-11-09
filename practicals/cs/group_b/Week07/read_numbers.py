#!/usr/bin/env python3


def read_yes_or_no(prompt):
    while True:
        answer = input(prompt + ': ')
        if answer in ['y', 'n', 'yes', 'no']:
            return answer


def read_positive_int(prompt, max_val, min_val):
    while True:
        try:
            num = int(input(prompt + ': '))
            if min_val <= num <= max_val:
                return num
            else:
                print('Value out of range!')
        except ValueError:
            print('Please enter an integer.')


if __name__ == '__main__':

    choice_1 = read_yes_or_no('Do you like cheese')
    choice_2 = read_yes_or_no('Do you like pineapple')
