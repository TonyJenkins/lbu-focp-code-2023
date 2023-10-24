from random import randint as rand

if __name__ == "__main__":

    class Test:

        def __init__(self, num_questions, max_num):
            self.num_questions = num_questions
            self.max_num = max_num
            self.score = 0
            self.question()
        #enddef

        def question(self):
            for i in range(self.num_questions):
                num_1 = rand(0, self.max_num)
                num_2 = rand(0, self.max_num)
                question = f"{str(num_1)} x {str(num_2)} = "
                actual_answer = str(num_1 * num_2)
                child_answer = input(question)
                if child_answer.strip() == actual_answer:
                    print("Correct!\n")
                    self.score += 1
                else:
                    print("That's not quite right!\n")
                #endif
            self.results()
            #endloop
        #enddef

        def results(self):
            incorrect = self.num_questions - self.score
            print(f"You answered {str(self.score)} questions correct and got {str(incorrect)} questions wrong!")
            if self.score > 5:
                print("Well done!")
            elif 2 < self.score < 5:
                print("You're getting there!")
            else:
                print("Try harder next time!")
            #endif
        #enddef
    #endclass

    #main starts here
    test = Test(10, 12)


#COMMENT
#Here is one using a Class Object and Instances - beyond the scope of this module, but may if time in the session to be talked through
