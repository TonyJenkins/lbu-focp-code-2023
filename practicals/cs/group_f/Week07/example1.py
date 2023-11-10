#!/usr/bin/env python3

#This file requires a text file to be passed as a CLA - numbers.txt is an example that can be used.
#It adds each line and writes the total to the file

import sys

if __name__ == '__main__':

    try:
        file = sys.argv[1]
    except IndexError:
        print('No CLAs given')
        exit()

    try:
        f = open(file, 'r+')
        line_number = 0
        total = 0
        for line in f:
            line_number += 1
            try:
                number = int(line)
                total += number
            except ValueError:
                print(f'Line {line_number} had an error - {line}', sep='', end='')
        f.write('\n')
        f.write(f'The sum of all valid integers is {total}')
        f.close()
    except FileNotFoundError:
        print('file not found')


