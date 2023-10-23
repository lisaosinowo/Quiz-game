from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"] 
    question_answer = question["answer"]
    # The loop loops through each dictionary in the list where the value is obtained using the "text" and "answer" keys
    new_question = Question(question_text, question_answer)
    # A new object is created each time in the loop with line 14 using the text and answer attributes
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()
    quiz.check_answer()

print("You have completed the quiz!")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")

