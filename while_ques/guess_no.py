# Write a while loop for a simple game where the user has to guess a number between 1 and 10. The loop should keep asking for guesses until the user guesses correctly.

import random

mn = 1
mx = 50
s_no = random.randint(mn,mx)
tries = 0

print("Welcome to the Number Guessing Game")
print(f"Guess the Number between {mn} to {mx}")

guess = 0

while guess != s_no:
    guess = int(input("Enter your guess: "))
    tries += 1
    if guess < s_no:
        print("Too low... Try again.")
    elif guess > s_no:
        print("Too high... Try again.")
    else:
        print("Congratulations! You guessed the correct number.")

print("Thanks for playing!")
print(f"Tries take {tries}")
