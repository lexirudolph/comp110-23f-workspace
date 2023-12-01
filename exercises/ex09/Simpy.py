"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730416818"


class Simpy:
    """My Simpy library!"""
    values: list[float]

    def __init__(self, values_init: list[float]):
        """Constructor."""
        self.values = values_init
        return None
    
    def __str__(self) -> str:
        """Converts input into a string representation."""
        return f"Simpy({self.values})"
    
    def fill(self, float: float, int: int) -> None:
        """Mutates the object fill is called on."""
        self.values = [float] * int
        return None
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attribute with a range of values."""
        if step == 0.0:
            raise ValueError("Step value cannot be 0.0.")
        current_val = start
        while (step > 0 and current_val < stop) or (step < 0 and current_val > stop):
            self.values.append(current_val)
            current_val += step

    def sum(self) -> float:
        """Computes the sum of all items in the values attribute."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """New Simpy object is produced where each item corresponds to the item at the same index on the left."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values), "Both Simpy objects must have equal lengths."
            result_values = [x + y for x, y in zip(self.values, rhs.values)]
        elif isinstance(rhs, float):
            result_values = [x + rhs for x in self.values]
        return Simpy(result_values)
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Similar to __add__ but exponential instead of addition."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values), "Both Simpy objects must have equal lengths."
            result_values = [x ** y for x, y in zip(self.values, rhs.values)]
        elif isinstance(rhs, float):
            result_values = [x ** rhs for x in self.values]
        return Simpy(result_values)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator overload for ==."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values), "Both Simpy objects must have equal lengths."
            result_mask = [x == y for x, y in zip(self.values, rhs.values)]
        elif isinstance(rhs, float):
            result_mask = [x == rhs for x in self.values]
        else:
            raise TypeError("Unsupported type for equality comparison. Must be a float or Simpy object.")
        return result_mask
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator overload for >."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values), "Both Simpy objects must have equal lengths."
            result_mask = [x > y for x, y in zip(self.values, rhs.values)]
        elif isinstance(rhs, float):
            result_mask = [x > rhs for x in self.values]
        else:
            raise TypeError("Unsupported type for equality comparison. Must be a float or Simpy object.")
        return result_mask
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Adds the ability to use the subscription operator with Simpy objects."""
        if isinstance(rhs, int):
            return self.values[rhs]
        elif isinstance(rhs, list) and all(isinstance(item, bool) for item in rhs):
            filtered_values = [x for x, mask_value in zip(self.values, rhs) if mask_value]
            return Simpy(filtered_values)
        else:
            raise TypeError("Unsupported type for indexing. Must be an int or a list of bools.")