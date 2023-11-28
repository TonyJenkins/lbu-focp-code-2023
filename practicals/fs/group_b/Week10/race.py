#!/usr/bin/env python3


from statistics import mean


def print_welcome():
    print('Park Run Timer')
    print('~~~~~~~~~~~~~~')
    print()
    print('Let\'s Go!')


def time_as_string(s):
    hours = s // 60
    mins = s % 60

    hour_word = 'hours' if hours > 1 else 'hour'
    mins_word = 'minutes' if mins > 1 else 'minute'

    return f'{hours} {hour_word}, {mins} {mins_word}'


if __name__ == '__main__':

    print_welcome()

    times = []
    runners = []

    while True:
        next_time = input('> ')

        if next_time == 'END':
            break

        try:
            race_number, race_time = next_time.split('::')

            runners.append(race_number)
            times.append(int(race_time))

        except ValueError:
            print('Invalid input.')

    try:
        print(f'Number of Runners: {len(times)}')

        print(f'Fastest Time: {time_as_string(min(times))}')
        print(f'Slowest Time: {time_as_string(max(times))}')
        print(f'Average Time: {mean(times):.2f}')

        print()
        print(f'Fastest Runner: {runners[times.index(min(times))]}')
        print()

    except ValueError:
        print('No data entered.')
