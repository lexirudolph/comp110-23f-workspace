"""EX04 - Utility functions."""

__author__ = "730416818"


def all(given_list: list[int], given_int: int) -> bool:
    """This function returns a boolean variable declaring whether the given integer is found in the given list."""
    i: int = 0
    c: int = 0
    if len(given_list) == 0:
        return False
    for i in given_list:
        if len(given_list) == 0:
            return False
        if given_list[0] != given_list[1]:
            return False
        if given_int != given_list[i]:
            return False
        if given_int == given_list[i]:
            c += 1
    i += 1
    if c == len(given_list):
        return True
    return bool


def max(input: list[int]) -> int:
    """This function returns the largest number (the maximum) of a given list of numbers."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    maximum = input[0]
    for i in input:
        if i > maximum:
            maximum = i
    return maximum
    

def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns boolean variable that indicates whether the two given lists are exactly equal."""
    a: int = 0
    if len(list1) == 0 and len(list2) == 0:
        return True
    if len(list1) == 0:
        return False
    elif len(list2) == 0:
        return False
    elif len(list1) != len(list2):
        return False
    
    if len(list1) == len(list2):
        while a <= len(list1):
            if list1[a] != list2[a]:
                return False
            else:
                return True
        a += 1
    return bool