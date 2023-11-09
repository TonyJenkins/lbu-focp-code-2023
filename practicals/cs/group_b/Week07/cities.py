#!/usr/bin/env python3


def chomp(s):
    return s[:-1]


def read_city_file(filename='cities.txt'):

    cities = {}

    with open(filename, 'r') as c:
        for line in c:
            country, capital = line.split(',')
            cities[country] = chomp(capital)

    return cities


def write_city_file(cities, filename='cities.txt'):
    with open(filename, 'w') as c:
        for country in cities:
            c.write(f'{country},{cities[country]}\n')


if __name__ == '__main__':

    cities = read_city_file()
    print(cities)

    country = input('Enter a country: ')
    if country.lower() in cities:
        print(f'The capital of {country.capitalize()} is {cities[country].capitalize()}.')
    else:
        capital = input('Enter the capital: ')
        cities[country] = capital

    write_city_file(cities)
