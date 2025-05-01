from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

Question_Bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    Question_Bank.append(new_question)

# print(Question_Bank)
quiz_brain = QuizBrain(Question_Bank)
# quiz_brain.next_question()

# print(quiz_brain.still_has_questions())

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print(f"You've completed the Quiz.")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")