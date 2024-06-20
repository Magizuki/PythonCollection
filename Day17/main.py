from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_list = []

for i in range(0, len(question_data)):
    question_list.append(Question(question_data[i]["text"], question_data[i]["answer"]))

quiz_brain = QuizBrain(question_list)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print('You have completed the quiz!')
print(f'Your final score was: {quiz_brain.score}/{len(quiz_brain.question_list)}')

