"""Summing the elements of a list using different loops."""

__author__ = "730416818"


def w_sum(vals: list[float]) -> float:
    """Takes a list of floats and returns the sum."""
    sum_w: float = 0.0    
    if len(vals) == 0:
        return sum_w
    index = 0
    while index < len(vals):
        sum_w += vals[index]
        index += 1
    return sum_w


def f_sum(vals: list[float]) -> float:
    """Takes a list of floats and returns the sum."""
    sum_f: float = 0.0    
    if len(vals) == 0:
        return sum_f
    for index in vals:
        sum_f += index
    return sum_f


def f_range_sum(vals: list[float]) -> float:
    """Takes a list of floats and returns the sum."""
    sum_r: float = 0.0
    if len(vals) == 0:
        return sum_r
    for index in range(len(vals)):
        sum_r += vals[index]
    return sum_r