import random

num1 = random.randint(1,10)
num2 = random.randint(1,10)

correct_answer = num1 * num2

user_answer =int(input(f"What is {num1} * {num2}?"))

if user_answer ==correct_answer:
    print("correct! well done.")
else:
    print(f"sorry, that's not correct.The answer is {correct_answer}.")


#COMMENT
#remember to include the if name == '__main__':
#this works as a single operation - wrap a for loop round it