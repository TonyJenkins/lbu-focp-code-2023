#!/usr/bin/env python3

if __name__ == '__main__':
    correct_ans = 0
    Equation_1 = int(input('5 x 5 = '))
    if Equation_1 == 25:
        correct_ans = correct_ans + 1
        print("Correct")
    else:
        print("Gah! That's not right!")
    Equation_2 = int(input('7 x 8 = '))
    if Equation_2 == 56:
        correct_ans = correct_ans + 1
        print("Correct")
    else:
        print("Gah! That's not right!")
    Equation_3 = int(input('9 x 4 = '))
    if Equation_3 == 36:
        correct_ans = correct_ans + 1
        print("Correct")
    else:
        print("Gah! That's not right!")
    Equation_4 = int(input('3 x 5 = '))
    if Equation_4 == 15:
        correct_ans = correct_ans + 1
        print("Correct")
    else:
        print("Gah! That's not right!")
    Equation_5 = int(input('1 x 10 = '))
    if Equation_5 == 10:
        correct_ans = correct_ans + 1
        print("Correct")
    else:
        print("Gah! That's not right!")

    print(f"You got {correct_ans} right!")

#COMMENT
#This is taking shape - but start to see which are variables and to recognise repetition.
#There are no prizes for writing short code - just readable code. Look at the model solution.