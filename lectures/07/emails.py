#!/usr/bin/env python3

from random import randint
import sys


DOMAIN = 'pop.ac.uk'


def line_split(infile_line):
    return infile_line[:8], infile_line[8:]


def find_capitals(s):
    return ''.join([c if c.isupper() else '' for c in s])


def to_initials(initials):
    return '.'.join(initials.lower())


def four_random_digits():
    rd = ''

    for _ in range(4):
        rd += str(randint(0, 9))

    return rd


def clean_surname(s):
    s = s.lower().strip()

    return ''.join([c if c.isalpha() else '' for c in s])


def build_email(name):

    surname, forenames = name.split(',')

    initials = to_initials(find_capitals(forenames))
    surname = clean_surname(surname)

    return f'{initials}.{surname}{four_random_digits()}@{DOMAIN}'


if __name__ == '__main__':

    try:
        with open(sys.argv[1], 'r') as infile, open('emails.txt', 'w') as outfile:
            for line in infile.readlines():

                user_id, name = line_split(line)

                outfile.write(f'{user_id} {build_email(name)}\n')

    except FileNotFoundError:
        print('File not found')
    except IndexError:
        print(f'{sys.argv[0]}: Missing CLA')
