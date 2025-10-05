import random

print("\nWelcome to the Number Guessing Game!")

print("\nTry to guess the number between 1 and 100.")
ri = random.randint(1,100)
at = 0

while 1:
    at += 1
    try:
        guess = int(input("\nEnter your guess: "))
    except ValueError:
        print("Enter a valid integer number.")
        continue
    if guess==ri:
        print(f"\nCongratulations! You've guessed the number in {at} attempts.")
        break
    elif guess>ri:
        print("Too high!")
    else:
        print("Too low!")