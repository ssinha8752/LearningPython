from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    new_q=Question(i['text'],i['answer'])
    question_bank.append(new_q)


new_quiz=QuizBrain(question_bank)

while new_quiz.still_has_questions():
    new_quiz.next_question()

print("Quiz Done!!")
print(f"Final Score is {new_quiz.score}/{new_quiz.question_number}")