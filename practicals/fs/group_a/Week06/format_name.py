#!/usr/bin/env python3

def format_name_case(str):
    first_letter = str[0].upper()
    remaining_letters = str[1:].lower()
    return first_letter + remaining_letters


if __name__ == '__main__':
    user_name = input('Please enter your name: ')
    user_name = format_name_case(user_name)
    print(f'Hello {user_name}, It is good to meet you')
