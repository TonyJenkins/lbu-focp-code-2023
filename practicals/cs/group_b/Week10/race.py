#!/usr/bin/env python3


from statistics import mean


def time_as_words(sec):
    mins = sec // 60
    secs = sec % 60

    mins_word = 'minutes' if mins > 1 else 'minute'
    secs_word = 'seconds' if mins > 1 else 'second'

    return f'{mins} {mins_word}, {secs} {secs_word}'


if __name__ == '__main__':

    times = []

    while True:

        race_line = input('> ')
        if race_line == 'END':
            break

        try:
            race_number, time_as_str = race_line.split('::')
            if len(race_number) > 0:
                times.append(int(time_as_str))
            else:
                raise ValueError
        except ValueError:
            print('Invalid Data.')

    print()
    print(f'Number of Runners: {len(times)}')
    print()
    print(f'Fastest Time: {time_as_words(min(times))}')
    print(f'Slowest Time: {time_as_words(max(times))}')
    print(f'Average Time: {time_as_words(mean(times))}')
