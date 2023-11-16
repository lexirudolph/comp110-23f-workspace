"""File to define Bear class."""

__author__ = "7304416818"


class Bear:
    """Class representing bears living in the river!"""
    age: int
    hunger_score: int

    def __init__(self, age_init: int = 0, hunger_score: int = 0):
        """Constructor."""
        self.age = age_init
        self.hunger_score = hunger_score
        return None
    
    def one_day(self):
        """Increase the value of age by 1 and decrease the hunger score by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Update bear's hunger score."""
        self.hunger_score += num_fish
        return None