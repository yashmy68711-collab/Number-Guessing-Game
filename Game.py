import random

print("Number Guessing Game")

number = random.randint(1, 100)
attempts = 0
max_attempts = 7

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess (1-100): "))
    except:
        print("Please enter a valid number")
        continue

    attempts += 1
    print("Attempts left:", max_attempts - attempts)

    if abs(guess - number) <= 5 and guess != number:
        print(" Very close!")

    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print("Correct! You guessed it in", attempts, "attempts 🎉")
        break

if attempts == max_attempts and guess != number:
    print("Game Over! The number was", number)
