### Guess the Number Game ###

import random

num = random.randint(1, 20)

print("I am thinking of a number between 1 and 20. Take a guess.")

guess = -1

while guess != num:
    guess = int(input())
    if guess < num:
        print("Too low!")
    else:
        print("Too high!")
    
print("Congratulations! You got it!")