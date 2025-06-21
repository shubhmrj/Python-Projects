class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score=0
        self.question_list = q_list

    def is_still_question(self):
      return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        a = input(f"q.{self.question_number}:{current_question.text} (True/False): ")

        if a == current_question.answer:
            print("You got it right!")
            print(f"The correct answer is {current_question.answer}")
            self.score+= 1
            print(f"{self.score}")


        else:
            print("No you don't got it :")
            print(f"The correct answer is {current_question.answer}")

