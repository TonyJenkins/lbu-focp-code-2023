#!/usr/bin/env python3


import sys


def remove_space(s):
    return ''.join([c for c in s if c != ' '])


def reverse_string(s):
    return s[::-1]


def obfuscate(m):
    m = remove_space(m)
    m = reverse_string(m)

    return m


if __name__ == '__main__':

    message = input('Enter the message: ')
    print(obfuscate(message))
