# Python CLI Quiz Game

This repository contains a simple, interactive command-line quiz game built with Python. It serves as a great introductory project for understanding core concepts like loops, conditional statements, user input, and working with data structures like lists and dictionaries.

The game welcomes the user, presents a series of multiple-choice questions, tracks the score, and provides feedback on the answers.

## Features

-   Interactive command-line interface with colored text for enhanced readability.
-   A series of multiple-choice questions.
-   Real-time score tracking, with 2 points awarded for each correct answer.
-   The final score is displayed upon completion of the quiz.
-   Easily customizable questions and answers directly within the script.

## Prerequisites

-   Python 3.13.3
-   `colorama` library

## Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/kaushik3207/quiz-game.git
    ```

2.  **Navigate to the project directory:**
    ```sh
    cd quiz-game
    ```

3.  **Install the required dependency:**
    The project uses the `colorama` library to display colored text in the terminal.
    ```sh
    pip install colorama
    ```

## How to Play

Run the script from your terminal using the following command:

```sh
python quizGame.py
```

The game will start by displaying a welcome message and instructions. It will then prompt you for your name and begin the quiz. For each question, enter the number corresponding to your chosen answer and press Enter.

## Customization

You can easily modify, add, or remove questions by editing the `questions` list at the beginning of the `quizGame.py` file.

Each question is a dictionary with the following structure:
-   `question`: The text of the question (string).
-   `options`: A list of possible answers (list of strings).
-   `correct`: The 0-based index of the correct answer in the `options` list (integer).
