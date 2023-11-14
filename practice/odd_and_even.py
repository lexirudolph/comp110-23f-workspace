"""QZ02 - Odd and Even."""

def odd_and_even(input: list[int]) -> list[int]:
    """Return a new list containing the elements of the input list that are odd and have an even index."""
    i: int = 0
    output: list[int] = []
    
    while i < len(input):
        if input[i] % 2 == 1 and i % 2 == 0:
            output.append(input[i])
        i += 1

    return output