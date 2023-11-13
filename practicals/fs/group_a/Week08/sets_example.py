#!/usr/bin/env python3

if __name__ == '__main__':
    my_word = 'hello world!'
    my_list = list(my_word)
    my_set = set(my_list)

    print(f'\nString Output - {my_word}')
    for i in my_word:
        print(i)

    print(f'\nList Output - {my_list}')
    for i in my_list:
        print(i)

    #running the program again will show that sets can not be indexed as positions will change
    #they are iterable but not indexable as no gurantee of position
    print(f'\nSet Output - {my_set}')
    for i in my_set:
        print(i)