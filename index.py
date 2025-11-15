import random

quiz = [
    {"question": "What is the correct file extension for Python files?", "answer": ".py"},
    {"question": "Which character is used to define a Python comment?", "answer": "#"},
    {"question": "Lists are created using ______ brackets.", "answer": "square"},
    {"question": "Tuples are used to store multiple items in a ______.", "answer": "single"},
    {"question": "Sets are written with ______ brackets.", "answer": "curly"},
    {"question": "Which keyword is used for working with files in Python?", "answer": "open"},
    {"question": "Which method removes the element at the specified position?", "answer": "pop"},
    {"question": "Which method adds an element at the end of the list?", "answer": "append"},
    {"question": "What function is used to get the length of a string?", "answer": "len"},
]

scores = []

def run_quiz():
    name = input("Enter your name: ")
    print(f"Welcome {name}! Let's start the quiz.\n")
    score = 0

    for i, q in enumerate(random.sample(quiz, len(quiz)), start=1):
        print(f"Question {i}: {q['question']}")
        if input("Your answer: ").strip().lower() == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.\n")

    print(f"\n{name}, your score is: {score}/10\n")
    scores.append({"name": name, "score": score})

def display_top_scores():
    print("Top Scores:")
    for i, s in enumerate(sorted(scores, key=lambda x: x['score'], reverse=True)[:3], start=1):
        print(f"{i}. {s['name']} - {s['score']}")

while input("Start quiz? (yes/no): ").strip().lower() == "yes":
    run_quiz()

display_top_scores()
