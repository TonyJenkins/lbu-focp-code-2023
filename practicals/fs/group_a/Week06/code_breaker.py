#!/usr/bin/env python3

#This is a template for the game where a computer picks a code consisting of 4 numbers 1->6 (no repeats)
#A player needs to crack the code, after each guess they are told how many are in the correct place
#and how many are valid numbers, but in the wrong place
#The functions need to be completed.

def make_computer_choice():
    # this function will need to return a list of 4 numbers - from a range of 1->6 with no number repeating
    return []


def validate_player_input(selection):
    # a function that will return True if the input is considered Valid, otherwise False
    return True


def get_input():
    # this function needs to return the player selection
    player_input = []
    while True:
        if validate_player_input(player_input):
            break
    return player_input


def get_matched_code_positions(a, b):
    # function that will return the number of matched items in a compared to b
    return 4


def get_number_contained_in_both(a, b):
    # function that will return the number of items contained in both a and b
    return 0


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
