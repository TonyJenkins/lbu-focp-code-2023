#!/usr/bin/env python3

import random

if __name__ == '__main__':
    sides = int(input('How many sides will the dice have?'))
    no_of_rolls = int(input('How many time shall the dice be rolled?'))
    all_rolls = []
    ratios = []

    for x in range(no_of_rolls):
        current_number = random.randint(1,sides)
        all_rolls.append(current_number)

    for x in range(sides):
        ratios.append(all_rolls.count(x+1))

    for x in range(sides):
        print(f"The number of {x+1}'s is {ratios[x]} and the percentage is {ratios[x]*100/no_of_rolls}")
   