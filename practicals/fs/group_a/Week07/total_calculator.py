#!/usr/bin/env python3

# this takes a file (CLA) and adds all numbers together and appends the file with the Total. 

import sys


if __name__ == '__main__':

    try:
        with open(sys.argv[1], 'r+') as f:
            print('File found.')
            total = 0
            for line in f:
                try:
                    total += int(line)
                except ValueError:
                    print("found dodgy data")
            print(total)
            f.write(f"Total is {total}")
    except FileNotFoundError:
        print('File not found')
    except IndexError:
        print(f'{sys.argv[0]}: Missing CLA')
