# Day-12-of-100-Number-guessing-game
Day 12 of 100 days of code python challenge, Angela Yu

Number Guessing Game (Day 12 of 100)

A simple Python command-line number guessing game where the player tries to guess a randomly generated number between 1 and 100 within a limited number of attempts.
This project is part of a 100 Days of Python challenge.


Features

Random number generation
Two difficulty levels:
    Easy – 10 attempts
    Hard – 5 attempts
Feedback after each guess:
    Too high
    Too low
    Correct guess
Game over message when attempts run out
Reveals the correct number if the player loses


How the Game Works

The program generates a random number between 1 and 100.
The user selects a difficulty level:
    easy → 10 attempts
    hard → 5 attempts
The player enters guesses.
After each guess the program tells the user whether the guess is:
    Too high
    Too low
    Correct
The game ends when:
    The player guesses the number correctly 🎉
    The player runs out of attempts ❌


Technologies Used

Python 3
Built-in random module


How to Run the Game

Make sure Python 3 is installed.
Download or clone the repository.
Run the script in the terminal:
Follow the prompts in the terminal.


Example Gameplay

Welcome to the number guessing game!
I am thinking of a number between 1 and 100

choose a difficulty, easy or hard?: easy
You have chosen easy mode, you have 10 attempts to guess the number.

What is your guess?: 50
Too high! guess again. You have 9 attempts left.

What is your guess?: 25
Too low! guess again. You have 8 attempts left.



Possible Improvements For Future Me

Add input validation for non-numeric guesses
Allow replaying the game
Add a score system
Add a GUI version using Tkinter or Pygame
Track number of games won/lost



