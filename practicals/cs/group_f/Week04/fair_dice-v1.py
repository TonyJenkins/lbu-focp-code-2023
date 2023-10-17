#!/usr/bin/env python3

import random

if __name__ == '__main__':
    no_of_rolls = int(input('How many time shall the dice be rolled?'))
    ones = twos = threes = fours = fives = sixes = 0

    for x in range(no_of_rolls):
        current_number = random.randint(1,6)
        if current_number == 1:
            ones = ones + 1
        elif current_number == 2:
            twos = twos + 1
        elif current_number == 3:
            threes = threes + 1
        elif current_number == 4:
            fours = fours + 1
        elif current_number == 5:
            fives = fives + 1
        elif current_number == 6:
            sixes = sixes + 1

    print(f'The number of ones is {ones} and the percentage is {ones*100/no_of_rolls}')
    print(f'The number of twos is {twos} and the percentage is {twos*100/no_of_rolls}')
    print(f'The number of threes is {threes} and the percentage is {threes*100/no_of_rolls}')
    print(f'The number of fours is {fours} and the percentage is {fours*100/no_of_rolls}')
    print(f'The number of fives is {fives} and the percentage is {fives*100/no_of_rolls}')
    print(f'The number of sixes is {sixes} and the percentage is {sixes*100/no_of_rolls}')