"""EX06 - Dictionary."""

__author__ = "730416818"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the inputed dictionary."""
    inverted_dict = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError("Duplicate key found. Cannot invert.")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Returns the most popular color of the given dictionary."""
    color_count = {}
    most_popular_color = None
    count = 0

    for name, color in input_dict.items():
        if color not in color_count:
            color_count[color] = 0
        color_count[color] += 1

        if color_count[color] > count:
            count = color_count[color]
            most_popular_color = color

    return most_popular_color


def count(input_list: list[str]) -> dict[str, int]:
    """Return a dictionary with a unique key and a corresponding value associated with the count of the unique value."""
    result_dict = {}
    for i in input_list:
        if i in result_dict:
            result_dict[i] += 1
        else:
            result_dict[i] = 1
    return result_dict


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Return a dictionary of keys in alphabetical order and values corresponding to the letter in the alphabet."""
    result_dict = {}

    for i in input_list:
        if len(i) > 0:
            first_letter = i[0].lower()
            if first_letter not in result_dict:
                result_dict[first_letter] = []
            result_dict[first_letter].append(i)
    return result_dict


def update_attendance(given_dict: dict[str, list[str]], x: str, y: str) -> dict[str, list[str]]:
    """Mutates a given dictionary to update attendance information."""
    if x in given_dict:
        given_dict[x].append(y)
    else:
        given_dict[x] = [y]
    return given_dict