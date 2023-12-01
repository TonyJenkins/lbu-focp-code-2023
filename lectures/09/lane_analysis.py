#!/usr/bin/env python3

from statistics import mean
import sys


def count_lanes(lanes, this_lane):

    return len([l for l in lanes if l == this_lane])


def count_speeders(speeds, speed_limit=30):
    return len([s for s in speeds if s > speed_limit])


def count_bus_lane_offenders(lanes, occupants):
    count = 0

    for check in range(len(lanes)):
        if lanes[check] == 'B' and occupants[check] < 2:
            count += 1

    return count


def print_stats(speeds, occupants, lanes):

    print()
    print('Data File Analysis')
    print('==================')
    print()
    print(f'Cars Seen: {len(speeds)}')
    print()
    print(f'Bus Lane:  {count_lanes(lanes, "B")}')
    print(f'Car Lane:  {count_lanes(lanes, "C")}')
    print()
    print(f'Average Speed: {mean(speeds)}')
    print()
    print(f'Speeders: {count_speeders(speeds)}')
    print(f'Bus Lane offenders: {count_bus_lane_offenders(lanes, occupants)}')


if __name__ == '__main__':

    speeds = []
    occupants = []
    lanes = []

    try:
        with open(sys.argv[1], 'r') as in_file:
            for line in in_file:
                speed, passengers, lane = line.strip().split(',')

                speeds.append(int(speed))
                occupants.append(int(passengers))
                lanes.append(lane)

    except (IndexError, FileNotFoundError,):
        print(f'Usage: {sys.argv[0]} <input file>')

    else:
        print_stats(speeds, occupants, lanes)
