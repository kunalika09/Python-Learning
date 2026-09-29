#NUMBER GUESSING GAME (with smart binary hints)
import random

#Generate a target data point between 1 and 50
target_number = random.randint(1, 50)
attempts = 0

print("--- BINARY LOGIC GUESSING GAME ---")
print("I'm thinking of a number between 1 and 50. Can you find it?")

while True:
    guess = input("Enter your guess:")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    guess = int(guess)
    attempts += 1

    if guess == target_number:
        print(f"Correct! You uncovered the target in {attempts} attempts.")
        break
    elif guess < target_number:
        print("Too low! Adjust your logic higher.")
    else:
        print("Too high! Adjust your logic lower.")
