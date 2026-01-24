# list of questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "answer": "2"
    },
    {
        "question": "How many days are there in a week?",
        "options": ["5", "6", "7", "8"],
        "answer": "3"
    },
    {
        "question": "What colour is the sky on a clear day?",
        "options": ["Green", "Blue", "Red", "Yellow"],
        "answer": "2"
    },
    {
        "question": "Which animal says 'meow'?",
        "options": ["Dog", "Cow", "Cat", "Sheep"],
        "answer": "3"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "2"
    },
    {
        "question": "Which season comes after spring?",
        "options": ["Winter", "Summer", "Autumn", "Spring"],
        "answer": "2"
    },
    {
        "question": "How many hours are there in one day?",
        "options": ["12", "18", "24", "36"],
        "answer": "3"
    }
]# Welcome message
print("Welcome to the Holton College Quiz!")
print("Please answer with 1, 2, 3, or 4.\n")

score = 0
question_number = 1

# Loop through each question
for question in questions:

    print("Question", question_number, ":", question["question"])

    # Display options
    option_number = 1
    for option in question["options"]:
        print(option_number, ".", option)
        option_number += 1

    # Get user input
    user_answer = input("Your answer: ")

    # Check answer
    if user_answer == question["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect.\n")

    question_number += 1

# Final result
print("Quiz Complete!")
print("You scored", score, "out of", len(questions))
print("Thank you for playing!")
# final version