"""EX03 - Structured Wordle."""

__author__ = "730416818"


secret: str = "codes"
c_match: str = ""
i: int = 0

def contains_char(word_search: str, char_search: str):
    """This function returns a boolean variable declaring whether the //
    given character is found in the given word."""
    assert len(char_search) == 1
    c: int = 0
    while c <= len(word_search):
        if char_search in word_search:
            return True
        else:
            return False
    c += 1

def emojified(guessed_word: str, secret_word: str):
    """Given two strings of the same length, a string of emojies will be //
    returned indicating which characters match and/or are contained in the guessed word."""
    assert len(guessed_word) == len(secret_word)
    global c_match
    global i
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    WHITE_BOX: str = "\U00002B1C"
    while i < len(guessed_word):
        if guessed_word[i] == secret_word[i]:
            c_match = c_match + GREEN_BOX
        elif guessed_word[i] in secret_word:
            c_match = c_match + YELLOW_BOX
        else:
            c_match = c_match + WHITE_BOX
        i = i + 1
    return c_match

def input_guess(n: int) -> int:
    """Given an integer of an expected length, the user will be prompted //
    to guess a word of the expected length."""
    game_guess: str = input(f"Enter a {n} character word: ")
    while len(game_guess) != int(n):
        guess_again: str = input(f"That was not {n} chars! Try again: ")
        game_guess = guess_again

    if len(game_guess) == (n):
        return (game_guess)
 
def main() -> None:
    """The entrypoint of the program and main game loop."""
    a: int = 0
    t: int = 1
    while a <= len(secret):
        print(f"=== Turn {t}/6 ===")
        wordle_guess: str = input_guess(len(secret))
        emojified(wordle_guess, secret)
        a += 1
        t += 1
        
        if wordle_guess == secret:
            if a == 1:
                return print(c_match) + print(f"You won in {a} try!")
            else:
                return print(c_match) + print(f"You won in {a} tries!")
        if a > len(secret):
            return print("X/6 - Sorry, try again tomorrow!")