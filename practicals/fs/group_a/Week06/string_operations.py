#!/usr/bin/env python3

def does_the_string_contain_spaces(text_input):
    return False


def count_characters_in_string(text_input):
    number = 0
    return number


def count_spaces_in_string(text_input):
    counter = 0
    return counter


if __name__ == '__main__':
    user_input = input('Please enter some text: ')

    if does_the_string_contain_spaces(user_input):
        print(f'Your input \'{user_input}\' contains at least one space')
        spaces_count = count_spaces_in_string(user_input)
        print(f'Your input \'{user_input}\' has {spaces_count} spaces')
    else:
        print(f'Your input \'{user_input}\' contains no space')

    letter_count = count_characters_in_string(user_input)
    print(f'Your input \'{user_input}\' has {letter_count} characters')


