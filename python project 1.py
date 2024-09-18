print("\033[34m -------Quiz Game--------- \033[0m")

questions = {
    "History": [
        {"question": "What year did World War II end?", "answer": "1945"},
        {"question": "Who was the first President of the United States?", "answer": "George Washington"},
    ],
    "Science": [
        {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
        {"question": "What is the process by which plants make food?", "answer": "Photosynthesis"},
    ],
    "Sports": [
        {"question": "Which team won the 2020 Super Bowl?", "answer": "Kansas City Chiefs"},
        {"question": "Who is the all-time leading scorer in the NBA?", "answer": "Kareem Abdul-Jabbar"},
    ],
}

high_scores = {}

def quiz_game():
    category = input("Select a category (History, Science, Sports): ")
    score = 0
    for question in questions[category]:
        user_answer = input(question["question"] + " ")
        if user_answer.lower() == question["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is " + question["answer"])
    print("Your final score is " + str(score) + " out of " + str(len(questions[category])))
    
    high_scores[category] = max(high_scores.get(category, 0), score)
    print("High Scores:")
    for category, score in high_scores.items():
        print(category + ": " + str(score))

while True:
    quiz_game()

