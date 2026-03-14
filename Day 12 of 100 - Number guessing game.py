## Day 12 of 100 - Number guessing game

# import random module to generate random number for computer to choose
import random


def check_guess(guess,computer_choice, attempts): # function to check if user's guess is correct, too high, or too low
    if guess == computer_choice:
        print("Congratulations! You guessed the number correctly.")
        return True
    elif guess > computer_choice:
        print("Too high!, guess again. You have", attempts - 1, "attempts left.")
    else:
        print("Too low!, guess again. You have", attempts - 1, "attempts left.")
    return False


print("Welcome to the number guessing game!",
      "I am thinking of a number between 1 and 100")

computer_choice = random.randint(1, 101) # computer generates a random number between 1 and 100
difficulty = input("choose a difficulty, easy or hard?: ").lower() # Prompt user for a difficulty level

attempts = 0

if difficulty == 'easy':
    attempts = 10
    print(f"You have chosen easy mode, you have {attempts} attempts to guess the number.")
elif difficulty == 'hard':
    attempts = 5
    print(f"You have chosen hard mode, you have {attempts} attempts to guess the number.")
else:
    print("Invalid difficulty level. Please choose 'easy' or 'hard'.") # handles edge cases where user inputs incorrectly


guess = int(input("What is your guess?: ")) # prompt user for thier guess

while attempts > 0: # Loop continues until user runs out of attempts or guesses correctly
    if check_guess(guess=guess, computer_choice=computer_choice, attempts=attempts):
        break
    attempts -= 1 # Decrease attempts by 1 after each guess
    if attempts == 0:
        print(f"Game over! You've used all your attempts. The correct number was {computer_choice}.")
        break # If user runs out of attempts, game is over and correct number is revealed
    guess = int(input("What is your guess?: "))



