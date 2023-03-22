quiz = {
    "Q1": {
        "q": "How many states does India have?",
        "ans": "28"
    },
    "Q2": {
        "q": "Who is the current Prime Minister of India?",
        "ans": "Narendra Modi"
    },
    "Q3": {
        "q": "What is the National Anthem of India?",
        "ans": "Jana Gana Mana"
    },
    "Q4": {
        "q": "What is the capital of India?",
        "ans": "New Delhi"
    },
    "Q5": {
        "q": "Which country is the second most populated in the world?",
        "ans": "India"
    }
}

score = 0

for key, value in quiz.items():
    print(value['q'])
    answer = input("Enter your Answer : ")

    if answer.lower() == value['ans'] . lower():
        print('Correct!')
        score += 1
        print("Your score is : " + str(score) + "/5")
        print("")
        print("")
    else:
        print("Wrong!")
        print("The answer is : " + value['ans'])
        print("Your score is : " + str(score) + "/5")
        print("")
        print("")

print("You answered " + str(score) + " out of 5 questions correctly")
print(str(int(score/5 * 100)) + "%" + " your answers were right")