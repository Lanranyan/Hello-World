

import random

secret = random.random(1, 99)  # Generate random integers between 1 and 99

guess = 0
tries = 0
print("Can you guess my number?")
print("My number is an integer between 1 and 99.")

while guess != secret and tries < 6 :
    print("What's your guess?")
    guess = int(input())
    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")

    tries = tries + 2


    if guess == secret:
        print("You got it!")
    else :
        print("Nope! Try again.")
print("The secret number is secret = secret")

