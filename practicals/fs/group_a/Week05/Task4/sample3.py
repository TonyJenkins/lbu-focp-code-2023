#!/usr/bin/env python3

if __name__ == '__main__':


    import random
    import math
    gamenumber = int(input("How many problems do you want?\n"))
    num_1 = random.randint(1,12)
    num_2 = random.randint(1,12)
    num_3 = (num_1*num_2)


    random.seed()
    count = 0
    while count < gamenumber:
        guess = int(input("What is " + str(num_1) + "x" + str(num_2) + "."))

        answer = (num_3)
        count +1
        correct = guess == answer

        if guess == answer:
            print("Correct!")
        else:
            print("WRONG. Its ", answer, ".")

    print('you did well')
    wrong == guess != answer

    result = correct/wrong

print("You got ", "%.1f"%result, "of the problems.")


#COMMENT
#This doesn't work - but looks interesting, can you spot the issues and resolve the code shown so that minor modifications will make it work?