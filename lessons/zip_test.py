"""Test my zip function!"""

__author__ = "730416818"

from lessons.zip import zip

def test_zip_different_lengths():
    """Testings the functione when provided two lists with different lengths."""
    test_list_str: list[str] = ["Leo", "Hans", "Franz"]
    test_list_int: list[int] = [1, 2]
    assert zip(test_list_str, test_list_int) == dict()


def test_zip_length_3():
    """Testing the function when provided two lists with 3 elements."""
    test_list_str: list[str] = ["Leo", "Hans", "Franz"]
    test_list_int: list[int] = [1, 2, 3]
    assert len(zip(test_list_str, test_list_int)) == 3


def test_empty_zip():
    """Testing the function with two empty lists."""
    test_list_str: list[str] = []
    test_list_int: list[int] = []
    assert zip(test_list_str, test_list_int) == dict()