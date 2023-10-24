import random

score = 0
TotalQuestions = 10

for i in range(TotalQuestions):
    number1 = random.randint(0, 12)
    number2 = random.randint(0, 12)

    Answer = number1 * number2
    Student_answer = int(input(f"{number1} * {number2} = "))
    if Student_answer == Answer:
        score += 1
        print("Well done! You got it right")
    else:
        print("It's incorrect, how disappointing..")


print("You finished the test! Here's how you did: ")
print(f"Score: {score} / 10 or {score * 10}%")

if score < 4:
    print("You didn't quite pass 40%, try again!")
else:
    print("You passed, well done!")

#COMMENT
#Please follow guidelines on well written code and include
#!/usr/bin/env python3
#if __name__ == '__main__':
#try to be more consistent in naming variables, here there is a mixture of lowercase and uppercase
