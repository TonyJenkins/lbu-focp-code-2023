#!/usr/bin/env python3


import sys

if __name__ == '__main__':

    args = sys.argv[1:]

    args.sort(key=len)
    print(args[0])
