"""EX07 - Dictionary Test!"""

__author__ = "730416818"

import pytest
from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance

from exercises.ex06.data_utils import main

class TestFunctions(unit_test.TestCase):

    def test_invert_expected_use1():
        """Testing the invert function when given diplicate keys."""
        with pytest.raises(KeyError):
            test_dict = {
                'a': 'one',
                'a': 'two'
            }
            invert(test_dict)


    def test_invert_expected_use2():
        """Testing the invert function when provided a dict with 3 elements."""
        test_dict: dict[str, str] = {
            "a": "one",
            "b": "two",
            "c": "three"
        }
        assert len(invert(test_dict)) == 3


    def test_invert_edge():
        """Testing the invert function with an empty."""
        test_dict: dict[str, str] = []
        assert invert(test_dict) == dict()


    #Favorite color tests
    def test_favorite_color_expected_use1():
        """Testing the favorite_color function when given a longer list."""
        test_dict = {
            'a': 'red',
            'b': 'red',
            'c': 'green',
            'd': 'blue',
            'e': 'red',
            'f': 'red',
            'g': 'green',
            'h': 'blue',
            }
        results = favorite_color(test_dict)
        assert results == 'red'


    def test_favorite_color_expected_use2():
        """Testing the favorite_color function when provided a tie result."""
        test_dict = {
            'a': 'red',
            'b': 'red',
            'c': 'green',
            'd': 'green',
            }
        results = favorite_color(test_dict)
        assert results == 'red'


    def test_favorite_color_edge():
        """Testing the favorite_color function with an empty dict."""
        test_dict: dict[str, str] = []
        assert invert(test_dict) == str


    #Count tests
    def test_count_expected_use1():
        """Testing an expected case for the count function."""
        input_list = ["a", "b", "a", "c", "b"]
        result = count(input_list)
        expected_result = {"a": 2, "b": 2, "c": 1}
        assert result == expected_result


    def test_count_expected_use2():
        """Testing an expected case for the count function."""
        input_list = ["red", "blue", "green", "red", "yellow", "blue", "red"]
        result = count(input_list)
        expected_result = {"red": 3, "blue": 2, "green": 1, "yellow": 1}
        assert result == expected_result


    def test_count_edge():
        """Testing an edge case for the count function."""
        input_list = []
        result = count(input_list)
        expected_result = {}
        assert result == expected_result


    #Alphabetizer tests
    def test_alphabetizer_expected_use1():
        """Testing an expected case for the alphabetizer function."""
        word_list = ["alpha", "beta", "charlie", "charles"]
        result = alphabetizer(word_list)
        expected_result = {"a": ["alpha"], "b": ["beta"], "c": ["charlie", "charles"]}
        assert result == expected_result


    def test_alphabetizer_expected_use2():
        """Testing an expected case for the alphabetizer function."""
        word_list = ["dog", "cat", "bird", "bug", "bear"]
        result = alphabetizer(word_list)
        expected_result = {"d": ["dog"], "c": ["cat"], "b": ["bird", "bug", "bear"]}
        assert result == expected_result


    def test_alphabetizer_edge():
        """Testing an edge case for the alphabetizer function."""
        word_list = ["", "123", "apple", "3_birds"]
        result = alphabetizer(word_list)
        expected_result = {"a": ["apple"], "o": ["birds"]}
        assert result == expected_result


    #Update attendance tests
    def test_ua_expected_use1():
        """Testing an expected case for the attendance function."""
        attendance_dict = {
            "Monday": ["Alice", "Bob"],
            "Tuesday": ["Charlie"],
        }
        day = "Monday"
        student = "Eve"
        result = update_attendance(attendance_dict, day, student)
        expected_result = {
            "Monday": ["Alice", "Bob", "Eve"],
            "Tuesday": ["Charlie"],
        }
        assert result == expected_result


    def test_expected_use_case_2():
        """Testing an expected case for the attendance function."""
        attendance_dict = {
            "Wednesday": ["Grace"],
        }
        day = "Wednesday"
        student = "David"
        result = update_attendance(attendance_dict, day, student)
        expected_result = {
            "Wednesday": ["Grace", "David"],
        }
        assert result == expected_result


    def test_edge_case():
        """Testing an edge case for the attendance function."""
        attendance_dict = {}
        day = "Thursday"
        student = "Frank"
        result = update_attendance(attendance_dict, day, student)
        expected_result = {
            "Thursday": ["Frank"],
        }
        assert result == expected_result