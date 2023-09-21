"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730416818"

guess: str = input("Enter a 5-character word: ")
if len(guess) == 5:
    character: str = input("Enter a single character: ")
    
    if len(character) == 1: 
        print("Searching for " + character + " in " + guess)
        count: int = 0
        if guess[0] == character:
            print(character + " found at index 0")
            count += 1
        if guess[1] == character:
            print(character + " found at index 1")
            count += 1
        if guess[2] == character:
            print(character + " found at index 2")
            count += 1
        if guess[3] == character:
            print(character + " found at index 3")
            count += 1
        if guess[4] == character:
            print(character + " found at index 4")
            count += 1
        
        if count == 1:
            print(str(count) + " instance of " + character + " found in " + guess)
        elif count == 0:
            print("No instances of " + character + " found in " + guess)
        else:
            print(str(count) + " instances of " + character + " found in " + guess)
    else:
        exit(print("Error: Character must be a single character."))
else:
    exit(print("Error: Word must contain 5 characters"))