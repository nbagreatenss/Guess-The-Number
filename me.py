#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

def guess_the_number():
    print("Welcome to Guess the Number Game!")
    print("Select Difficulty:")
    print("1. Easy (10 attempts)")
    print("2. Hard (5 attempts)")

    while True:
        difficulty = input("Enter 1 for Easy or 2 for Hard: ")
        if difficulty == '1':
            attempts = 10
            break
        elif difficulty == '2':
            attempts = 5
            break
        else:
            print("Invalid input. Please enter 1 or 2.")

    number_to_guess = random.randint(1, 100)
    print(f"You have {attempts} attempts to guess the number between 1 and 100.")

    for attempt in range(1, attempts + 1):
        while True:
            try:
                guess = int(input(f"Attempt {attempt}: Enter your guess: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempt} attempts.")
            break
    else:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

guess_the_number()