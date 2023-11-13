#!/usr/bin/env python3

def characters_in_at_least_one_of_words(a, b):
    return []


def characters_in_both_words(a, b):
    return []


def characters_in_just_one_of_words(a, b):
    return []


if __name__ == '__main__':
    word1 = input('Please enter the first word: ')
    word2 = input('Please enter the second word: ')

    print(f'These letters appear in at least one of the words {characters_in_at_least_one_of_words(word1, word2)}')
    print(f'These letters appear in both words {characters_in_both_words(word1, word2)}')
    print(f'These letters appear in just one of the words {characters_in_just_one_of_words(word1, word2)}')
