"""Combining two lists into a dictionary."""

__author__ = "730416818"


def zip(list_str: list[str], list_int: list[int]) -> dict[str, int]:
    """Create a dictionary from two lists."""
    zip_dict: dict[str, int] = dict()
    if len(list_str) != len(list_int):
        return zip_dict
    i: int = 0
    for elem in list_str:
        zip_dict[elem] = list_int[i]
        i += 1
    return zip_dict