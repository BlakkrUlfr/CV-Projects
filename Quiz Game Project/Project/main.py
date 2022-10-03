from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Write a for loop to iterate over the question_data
# Construct a Question Object From Each Entry in question_data
# Append Each Question Object to the question_bank

question_bank = []

# for number in range(12):
#     question = Question(question_data[number]['text'], question_data[number]['answer'])
#     question_bank.append(question)

for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
