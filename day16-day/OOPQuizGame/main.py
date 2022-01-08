from typing import ClassVar
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

new_quiz = QuizBrain(question_bank)

while new_quiz.still_ask_question():
    new_quiz.next_question()


print("Quiz is finished. You've completed it!")
print(f"Your final score was: {new_quiz.score}/{new_quiz.question_number}")
