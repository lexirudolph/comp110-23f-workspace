"""EX02: One shot Wordle!"""
__author__ = "730416818"

word: str = "python"
guess: str = input("What is your 6 letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

match: str = ""
i: int = 0

while len(guess) != int(6):
    guess_again: str = input("That was not 6 letters! Try again: ")
    guess = guess_again

if len(guess) == 6:
    while i < len(guess):
        if guess[i] == word[i]:
            match = match + GREEN_BOX
        elif guess[i] in word:
            match = match + YELLOW_BOX
        else:
            match = match + WHITE_BOX
        i = i + 1
    
    if guess != word:
        print(match)
        print("Not quite. Play again soon!")
    
    if guess == word:
        print(match)
        print("Woo! You got it!")