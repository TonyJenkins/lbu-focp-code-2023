#!/usr/bin/env python3

if __name__ == '__main__':
    while True:
        try:
            my_input = input("please enter a valid integer: ")
            my_input = int(my_input)
            break
        except ValueError:
            print(f'{my_input} is not valid: try again')

    print(f'{my_input} is valid: well done')