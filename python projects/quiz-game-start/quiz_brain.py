class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        question_object = self.question_list[self.question_number]
        question_text = question_object.text
        correct_answer = question_object.answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {question_text} (True/False): ").lower()
        self.check_answer(user_answer, correct_answer)



    def still_has_questions(self):
        if len(self.question_list) > self.question_number:
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


