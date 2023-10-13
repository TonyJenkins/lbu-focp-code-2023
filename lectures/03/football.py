#!/usr/bin/env python3

if __name__ == '__main__':

    margins = []

    for matches in range(5):

        result = input('Enter a result: ')

        goals_for = int(result.split('-')[0])
        goals_against = int(result.split('-')[1])

        margins.append(goals_for - goals_against)

    biggest_win = max(margins)
    biggest_defeat = abs(min(margins))
    goal_difference = sum(margins)

    print()
    print(f'Biggest Win:  {biggest_win}.')
    print(f'Biggest Loss: {biggest_defeat}.')
    print(f'Goal Diff:    {goal_difference}.')
