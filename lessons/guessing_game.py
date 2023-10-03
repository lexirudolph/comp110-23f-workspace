"""Game that only completes when you guess the right number"""

from random import randint

secret: int = randint(1,10)

guess: int = int(input("Guess a number between 1 and 10: "))

while guess != secret:
    print("Wrong!")
    guess = int(input("Guess again: "))
print("You got it!")