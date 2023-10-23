#!/usr/bin/env python3

if __name__ == '__main__':

        eight_temp = int(input("Enter 8am temp")[:-1])
        ten_temp = int(input("Enter 10am temp")[:-1])
        twelve_temp = int(input("Enter 12am temp")[:-1])
        two_temp = int(input("Enter 2pm temp")[:-1])
        four_temp = int(input("Enter 4pm temp")[:-1])
        six_temp = int(input("Enter 6pm temp")[:-1])


        Highest = max(eight_temp, ten_temp, twelve_temp, two_temp, four_temp, six_temp)
        lowest = min(eight_temp, ten_temp, twelve_temp, two_temp, four_temp, six_temp)

        Average =(eight_temp + ten_temp + twelve_temp + two_temp + four_temp + six_temp) / 6

        print()
        print(f'Highest temp: {Highest}.')
        print(f'Lowest temp:  {lowest}.')
        print(f'Average temp: {Average}.')

        print(f'The highest temp was {Highest}, the lowest was {lowest}'
              f' and the average as {Average}.')


#COMMENT
#this works as requested - while the task description didn't mention decimal places, it would be good to add for the average
#try to be consistent in variable naming - having both upper and lower case naming leads to confusion on whether there is significance to this.
#convention would have lower case
#the repetition on lines 5-10, prompts the thought of using a for loop