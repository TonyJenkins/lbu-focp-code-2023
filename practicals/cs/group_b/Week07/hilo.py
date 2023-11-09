#!/usr/bin/env python3

from random import randint


def generate_secret_number():
    while True:
        number = randint(0, 100)
        if number not in [25, 50, 75]:
            return number


def get_guess():

    while True:
        try:
            my_guess = int(input('Enter your guess: '))
            if 0 <= my_guess <= 100:
                return my_guess
            else:
                print('Guess out of range!')

        except ValueError:
            print('Please enter an integer!')


if __name__ == '__main__':

    secret = generate_secret_number()
    guesses = 0

    while True:

        guess = get_guess()
        guesses += 1

        if secret == guess or guesses == 10:
            break

        print(f'My number is {"higher" if secret > guess else "lower"} than that.')

    if guesses == 10 and guess != secret:
        print('You ran out of guesses!')
    else:
        print('Correct!')
