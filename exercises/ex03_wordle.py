"""EX03 - Structured Wordle."""

__author__ = "730416818"

def contains_char(char_search: str, word_search: str):
    """This function returns a boolean variable declaring whether the given character is found in the given word."""
    assert len(char_search) == 1
    if char_search[0] in word_search:
        return True
    else:
        return False


#def emojified(guessed_word: str, secret_word: str):
    """Given two strings of the same length, a string of emojies will be returned indicating which characters match and/or are contained in the guessed word."""
    
    guess: str = input("Enter a 5 character word: ")
    secret: str = "codes"
    
    match: str = ""
    i: int = 0

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    assert len(guessed_word) == len(secret_word)
    while i < len(guess):
        if guess[i] == secret[i]:
            match = match + GREEN_BOX
        elif guess[i] in secret:
            match = match + YELLOW_BOX
        else:
            match = match + WHITE_BOX
        i = i + 1