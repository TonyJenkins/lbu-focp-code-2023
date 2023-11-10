#!/usr/bin/env python3

#This file uses a modified cat_shelter_1.txt to check if a line contains 2 ','

def is_line_valid(line):
    if line.count(',') == 2:
        return True
    else:
        return False


if __name__ == '__main__':
    try:
        f = open('cat_shelter_1.txt', 'r')
        line_number = 0
        for line in f:
            line_number += 1
            if is_line_valid(line) == False:
                print(f'Line {line_number} had an error - {line}', sep='', end='')
        f.close()
    except FileNotFoundError:
        print('file not found')
