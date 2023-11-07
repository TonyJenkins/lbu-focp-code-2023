#!/usr/bin/env python3


import sys

if __name__ == '__main__':

    try:
        f = open(sys.argv[1], 'r')
        print('File exists!')
    except FileNotFoundError:
        print('File does not exist!')
    except IndexError:
        print('Error! Missing the file name!')
