# Task 3
## Temperature Facts

A weather station takes readings every two hours through the day, from 8am to 6pm. A program is required that will find the highest, lowest, and average temperature through the day.

The temperature is entered as a string, for example:

    Enter 8am temp: 11C
    Enter 10am temp: 13C

and so on. There is no need to worry about validating the data entered. All temperatures are integer values.

The final output should be the highest, lowest, and average temperature through the day. Use a format something like:

    Highest Temp: 18C
    Lowest Temp:   9C
    Average Temp: 13.5C

Do not worry if you don't get all the details. Commit a version that includes as much as you have done. The below may help with the trickier parts.

### Hints

That pesky 'C':

    >>> temp = '11C'
    >>> temp[:-1]
    '11'

The time in the prompt:

    >>> for s in ['one', 'two', 'three']:
    ...   print(s)
    ... 
    one
    two
    three


