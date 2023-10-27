#!/usr/bin/env python3

if __name__ == '__main__':

    try:
        f = open('football.py', 'r')

    except FileNotFoundError:
        print('File not found')
