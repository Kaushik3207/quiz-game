import time

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["New Delhi", "Mumbai", "Kolkata", "Chennai"],
        "correct" : 0
    },
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "correct": 0  # Index of the correct answer
    },
    {
        "question": "Which city is known as the Pink city?",
        "options": ["Jaipur", "Agra", "Delhi", "Mumbai"],
        "correct": 0
    }
]

def main():
    print("Welcome to the Quiz Game!")
    print("----------------------------------")

def display_welcome():
    print("****************************************************")
    print("*                                                   *")
    print("*           WELCOME TO THE QUIZ GAME!              *")
    print("*                                                   *")
    print("****************************************************")
    print("\n")

    #game instructions
    from colorama import Fore, Back, Style

    print(Fore.RED + "Instructions:")
    print(Fore.RED + "1. You will be asked a series of questions.")
    print(Fore.RED + "2. Each question will have multiple choice answers.")
    print(Fore.RED + "3. Type the number corresponding to your answer.")
    print(Fore.RED + "4. You will receive points for each correct answer.")
    print(Fore.RED + "5. The game ends when you answer all questions or choose to exit.")

    #get user name
    userName = input("Please enter your name: ")
    print(Fore.GREEN + f"Hello {userName}! let's get started!\n")
    time.sleep(3)  # Pause for 3 seconds before starting the game

    print("\n" * 25) # Clear the screen by printing new lines

def startGame():
    playGame = True
    gameActive = True
    currentScore = 0
    score = 0
    totalQuestions = 3
    currentQuestion = 0
    while gameActive and playGame:
        time.sleep(1)  # Pause for 1 second before displaying the next question

        print("\nCurrent Score:", currentScore)
        current = questions[currentQuestion]
        print("\nQuestion:", current["question"])
        print("Options:")

        for i, option in enumerate(current["options"]):
            print(f"{i+1}. {option}")

        while True:
            userAnswer = input("Please enter your answer (1-4) or type quit to exit the game: ")
            if userAnswer.lower() == "quit":
                print("Thank you for playing!")
                gameActive = False
                playAgain = False
                playGame = False
                print("\nExiting the game...")
                time.sleep(1)  # Pause for 1 second before exiting
                print("Your final score is:", currentScore)
                break
            elif userAnswer.isdigit() and 1 <= int(userAnswer) <= 4:
                    userAnswerIndex = int(userAnswer) - 1
                    currentQuestion += 1
                    if userAnswerIndex == current["correct"]:
                        score += 2
                        currentScore += 2
                        print("Correct!")
                        print("Your current score is:", currentScore)
                        break
                    else:
                        print("Incorrect! The correct answer was:", current["options"][current["correct"]])
                        break
            else:
                print("Invalid input. Please enter a number between 1 and 4 or type quit to exit.")

        if currentQuestion >= totalQuestions:
            gameActive = False
            playGame = False
            print("You have answered all questions!")
            from colorama import Fore
            print(Fore.YELLOW + "Congratulations! You have completed the quiz.")
            print(Fore.WHITE + "Your final score is: " + str(score) + " out of " + str(totalQuestions * 2))
            break
    print("Thank you for playing the Quiz Game!")




if __name__ == "__main__":
    main()
    display_welcome()
    startGame()