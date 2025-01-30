from random import *

def guess_number():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    number = randint(1, 20)
    popitka = 0

    while True:
        guess = int(input("Take a guess: "))
        popitka += 1
        if guess == number:
            print(f"Good job, {name}! You guessed my number in {popitka} guesses!")
            break
        elif guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high")


guess_number()