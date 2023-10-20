#!/usr/bin/env python3

if __name__ == '__main__':
    name = input('Hello! What is your name? ')

    if len(name) > 0:
        print(f'Well met, {name}! It is good to meet you!')
    else:
        print('Well met, Mysterious Stranger! How shall we learn your name?')
