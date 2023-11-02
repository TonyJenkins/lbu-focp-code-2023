#!/usr/bin/env python3

import random


def make_computer_choice():
    numbers = ['1', '2', '3', '4', '5', '6']
    random.shuffle(numbers)
    return numbers[:-2]


def validate_player_input(selection):
    if len(selection) != 4:
        return False
    for x in selection:
        if x not in ['1', '2', '3', '4', '5', '6']:
            return False

    return True


def get_input():
    while True:
        player_input = input('Please enter a 4 digit code using just the numbers 1->6:')
        if validate_player_input(player_input):
            break
    return list(player_input)


def get_matched_code_positions(a, b):
    count = 0
    for x in range(len(a)):
        if a[x] == b[x]:
            count += 1
    return count


def get_number_contained_in_both(a, b):
    count = 0
    for x in a:
        if x in b:
            count += 1
    return count


if __name__ == '__main__':
    comp_selection = make_computer_choice()
    turns = 0
    while True:
        player_selection = get_input()
        turns += 1
        correct_positions = get_matched_code_positions(player_selection, comp_selection)
        print(f'You have {correct_positions} in your selection that match exactly the computer choice')
        if correct_positions == 4:
            break
        correct_numbers = get_number_contained_in_both(player_selection, comp_selection)
        print(f'You have {correct_numbers - correct_positions} that are in the computer choice, but wrong position')

    print(f'Well Done - You broke the code {comp_selection} in {turns} turns')
