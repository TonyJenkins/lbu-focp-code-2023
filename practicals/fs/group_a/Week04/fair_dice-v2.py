#!/usr/bin/env python3

import random

if __name__ == '__main__':
    no_of_rolls = int(input('How many time shall the dice be rolled?'))
    all_rolls = []

    for x in range(no_of_rolls):
        current_number = random.randint(1,6)
        all_rolls.append(current_number)

    ones = all_rolls.count(1)
    twos = all_rolls.count(2)
    threes = all_rolls.count(3)
    fours = all_rolls.count(4)
    fives = all_rolls.count(5)
    sixes = all_rolls.count(6)

    print(f'The number of ones is {ones} and the percentage is {ones*100/no_of_rolls}')
    print(f'The number of twos is {twos} and the percentage is {twos*100/no_of_rolls}')
    print(f'The number of threes is {threes} and the percentage is {threes*100/no_of_rolls}')
    print(f'The number of fours is {fours} and the percentage is {fours*100/no_of_rolls}')
    print(f'The number of fives is {fives} and the percentage is {fives*100/no_of_rolls}')
    print(f'The number of sixes is {sixes} and the percentage is {sixes*100/no_of_rolls}')