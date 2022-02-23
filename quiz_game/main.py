from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for dictionary in question_data:
    new_question = Question(dictionary["question"], dictionary["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank) #initializing quiz object
quiz.next_question() #initializing method in QuizBrain class

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"You're final score was: {quiz.score}/{len(question_bank)}")