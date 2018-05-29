#!/usr/bin/env python3

import random

random_number = random.randint(1,10)
guess = None

while True:
    guess = input("Pick a Guess from 1 to 10: ")
    guess = int(guess)
    if guess < random_number:
        print("It's LOW, raise ya number")
    elif guess > random_number:
        print("It's HIGH, lower thy number")
    else:
        print("Good Catch!!")
        play_again = input("Do you wanna play with luck? (y/n) ")
        if play_again == "y":
            random_number = random.randint(1,10) # numbers 1 - 10
            guess = None
        else:
            print("Thanks for the play")
            break

