#!/usr/bin/env python3

if __name__ == '__main__':

    margins = []

    while True:

        result = input('Enter a result: ')

        try:
            goals_for = int(result.split('-')[0])
            goals_against = int(result.split('-')[1])

            if goals_for >= 0 and goals_against >= 0:
                margins.append(goals_for - goals_against)
            else:
                print('Invalid result!')

            if len(margins) == 5:
                break

        except IndexError:
            print('Invalid format!')
        except ValueError:
            print('Invalid format!')

    biggest_win = max(margins)
    biggest_defeat = abs(min(margins))
    goal_difference = sum(margins)

    print()
    print(f'Biggest Win:  {biggest_win}.')
    print(f'Biggest Loss: {biggest_defeat}.')
    print(f'Goal Diff:    {goal_difference}.')
