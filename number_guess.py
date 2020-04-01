# Guess the number game
# GCB 4/1/2020
# Select a random number
import random
import math


def get_number():
    # get a random number between 1 and 10
     return random.randint(1,10)

# Prompt user to guess the number
print ('Welcome to the Number Guesser Game!')

# Setup
target = get_number()
print('target = ', target)
guess = int(input('Guess my number from 1-10? '))

# Loop if incorrect
while (guess != target):
    if guess < target:
        guess = int(input('That wasn\'t my number. Too low! Guess again: '))
    elif guess > target:
        if guess > 10:
            guess = int(input('Way too high! Guess again: '))
        else:
            guess = int(input('That wasn\'t my number. Too high! Guess again: '))

# Display winning prompt if guessed correctly
print('You guessed my number!')
