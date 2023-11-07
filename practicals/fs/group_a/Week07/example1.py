#!/usr/bin/env python3

#This file uses a modified cat_shelter_1.txt to check if a line contains 2 ',' 

import sys

def is_line_valid(line):
    if line.count(',') != 2:
        return False
    return True


if __name__ == '__main__':

    try:
        f = open(sys.argv[1], 'r')
        line_count = 1
        error_count = 0

        for line in f:
            if is_line_valid(line) == False:
                print(f'Error on line {line_count}: Line is {line}')
                error_count += 1
            line_count += 1
        if error_count==0:
            print("No issues with file")
        f.close()
    except FileNotFoundError:
        print('File not found')
    except IndexError:
        print(f'{sys.argv[0]}: Missing CLA')
