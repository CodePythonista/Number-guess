########## TASK ############


# Recreate this program in an OOP fashion
# Your class should have one attribute. This will be x
# This attribute will be a paramater in your init function

# GOOD LUCK !

## I should be able to call the function as so ...

## objectname.guess()

import random



##def guess(x):
##    # generates a random number between entry 1, entry 2
##    random_number = random.randint(1, x)
##    guess = 0
##    while guess != random_number:
##        guess = int(input(f'Guess a number between 1 and {x}: '))
##        if guess < random_number:
##            print('Sorry, guess again. Too low.')
##        elif guess > random_number:
##            print('Sorry, guess again. Too high.')
##
##    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')
##
##guess(10)

class Puzzle():

    def __init__(self, x):
         """Initialize x"""
         self.x = x
         
    def guess(self):
        """ Pick your number"""
    
    # generates a random number between entry 1, entry 2
        random_number = random.randint(1, self.x)
        guess = 0
        while guess != random_number:
            guess = int(input(f'Guess a number between 1 and {self.x}: '))
            if guess < random_number:
                print('Sorry, guess again. Too low.')
            elif guess > random_number:
                print('Sorry, guess again. Too high.')

        print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')


num = Puzzle(10)
num.guess()

