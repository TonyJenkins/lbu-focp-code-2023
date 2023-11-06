#!/usr/bin/env python3


import names
from random import choice as pick, randint
from string import digits
import sys


NAMES_FILE = 'students.txt'
NUMBER_OF_NAMES = 128
UCAS_CODE_LENGTH = 7
UCAS_PREFIX = 'c'


def generate_ucas_code(prefix='c', length=8):
    code = prefix
    for count in range(length):
        code += pick(digits)

    return code


def generate_name():
    forenames = randint(1, 3)
    gender = 'male' if randint(1, 2) == 1 else 'female'

    name = names.get_last_name()
    name += ', '
    name += ' '.join([names.get_first_name(gender) for count in range(forenames)])

    return name


def generate_line():
    return generate_ucas_code(UCAS_PREFIX, UCAS_CODE_LENGTH) + ' ' + generate_name()


if __name__ == '__main__':

    try:
        out_file = sys.argv[1]
    except IndexError:
        out_file = NAMES_FILE

    with open(out_file, 'w') as out:
        for line in range(NUMBER_OF_NAMES):
            out.write(generate_line() + '\n')
