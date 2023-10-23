#!/usr/bin/env python3

if __name__ == '__main__':
    temp_1 = int(input('Enter 8am temp #1: '))
    temp_2 = int(input('Enter 10am temp #2: '))


    max_temp = max(temp_1, temp_2)
    min_temp = min(temp_1, temp_2)
    avg_temp = (temp_1 + temp_2)/2

    print(f'Highest Temp: {max_temp}')
    print(f'Lowest Temp:  {min_temp}')
    print(f'Average Temp: {avg_temp:.2}')


#COMMENTS
#This is a part solution - it will work for a limited number of entries
#Start to recognise repetition and when it is seen, think of for loops and lists