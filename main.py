# Dictionary to hold data
questions = [
    {
        "question": "What is the most common cat breed?",
        "a": "Domestic Shorthair",
        "b": "Maine Coon",
        "c": "Siamese Cat",
        "d": "American Shorthair",
        "correct": "a"
    },
    {
        "question": "Which breed is known for its striking blue eyes?",
        "a": "Persian",
        "b": "Siamese",
        "c": "Bengal",
        "d": "Scottish Fold",
        "correct": "b"
    },
    {
        "question": "What is the average lifespan of an indoor cat?",
        "a": "5-7 years",
        "b": "10-15 years",
        "c": "15-20 years",
        "d": "20-25 years",
        "correct": "b"
    },
    {
        "question": "Which breed is famous for its polydactyl (extra toes) trait?",
        "a": "Sphynx",
        "b": "Maine Coon",
        "c": "Hemingway Cat",
        "d": "Norwegian Forest Cat",
        "correct": "c"
    },
    {
        "question": "What is the largest domesticated cat breed?",
        "a": "Sphynx",
        "b": "Maine Coon",
        "c": "Savannah",
        "d": "Bengal",
        "correct": "b"
    },
    {
        "question": "Which cat breed is known for its curly fur?",
        "a": "Siamese",
        "b": "Devon Rex",
        "c": "Bengal",
        "d": "British Shorthair",
        "correct": "b"
    },
    {
        "question": "What do cats use their whiskers for?",
        "a": "Hearing",
        "b": "Balance",
        "c": "Measuring space",
        "d": "Smelling",
        "correct": "c"
    },
    {
        "question": "Which breed is known for its distinctive folded ears?",
        "a": "Scottish Fold",
        "b": "American Curl",
        "c": "Sphynx",
        "d": "Burmese",
        "correct": "a"
    },
    {
        "question": "What is the primary reason cats purr?",
        "a": "Happiness",
        "b": "Hunger",
        "c": "Fear",
        "d": "Comfort",
        "correct": "d"
    },
    {
        "question": "Which cat breed is known for its playful and dog-like behavior?",
        "a": "Bengal",
        "b": "Sphynx",
        "c": "Ragdoll",
        "d": "Russian Blue",
        "correct": "a"
    }
]

# Function to ask user to play
def greeting():
    return input("Do you want to play (enter y)? ").lower() == "y"

# Display quiz
def quiz():
    print("Let's play!")
    score = 0
    # Iterate through each question
    for question in questions:
        answer = input(f"{question['question']}\nA. {question['a']}\nB. {question['b']}\nC. {question['c']}\nD. {question['d']}\nYour answer: ")
        if answer.lower() == question["correct"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['correct']}\n")
    
    print(f"Your final score is {score}/{len(questions)}")

# Run code
def main():
    print("Welcome to my cat quiz!")
    playing = greeting()
    if playing:
        quiz()
    else:
        print("Have a nice day!")

if __name__ == "__main__":
    main()
