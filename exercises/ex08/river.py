"""File to define River class."""

__author__ = "730416818"


from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """River environment with animals!"""
    day: int
    bears: list
    fish: list
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove animals from river because of age."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]
        return None
    
    def remove_fish(self, amount: int):
        """Removes the frontmost amount of fish."""
        self.fish = self.fish[amount:]
        return None

    def bears_eating(self):
        """Bears eat 3 fish if there are at least 5 present."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Removing bear if it starves."""
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        return None
        
    def repopulate_fish(self):
        """Each pair of fish produce 4 offspring."""
        offspring = []
        for i in range(0, len(self.fish), 2):
            offspring.extend([Fish() for i in range(4)])
        self.fish.extend(offspring)
        return None
    
    def repopulate_bears(self):
        """Each pair of bears produce 1 offspring."""
        offspring = []
        for i in range(0, len(self.bears), 2):
            baby_bear = Bear()
            offspring.append(baby_bear)
        self.bears.extend(offspring)
        return None
    
    def view_river(self):
        """Print river status."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate a week in the river."""
        week: list = [1, 2, 3, 4, 5, 6, 7]
        for day in week:
            self.one_river_day()
        return None