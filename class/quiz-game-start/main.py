
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    question_object = Question(question['text'],question['answer'])
    question_bank.append(question_object)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the Quiz.")
print(f"Your Final Score is : {quiz.score}/{quiz.question_number}")