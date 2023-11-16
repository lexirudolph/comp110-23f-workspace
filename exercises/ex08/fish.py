"""File to define Fish class."""

__author__ = "730416818"


class Fish:
    """Class representing the fish in the river!"""
    age: int

    def __init__(self, age_init: int = 0):
        """Constructor."""
        self.age = age_init
        return None
    
    def one_day(self):
        """Increase the value of age by 1."""
        self.age += 1
        return None