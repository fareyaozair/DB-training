import pytest
from highest_number_finder import HighestNumberFinder

def test_array_of_one_item_returns_this_itemy():
    # arrange
    numbers = [33]
    expectedResult = 33
    cut = HighestNumberFinder()

    # act
    result = cut.find_highest_number(numbers)
    # assert

    assert expectedResult == result

def test_find_highest_in_array_of_two_descending():
    # arrange
    numbers = [14, 7]
    expectedResult = 14
    cut = HighestNumberFinder()

    # act
    result = cut.find_highest_number(numbers)
    # assert

    assert expectedResult == result

def test_find_highest_in_array_of_two_ascending():
    # arrange
    numbers = [7, 14]
    expectedResult = 14
    cut = HighestNumberFinder()

    # act
    result = cut.find_highest_number(numbers)
    # assert

    assert expectedResult == result

def test_empty_array():
    numbers = []
    cut = HighestNumberFinder()

    with pytest.raises(Exception):
        assert cut.find_highest_number(numbers)

def test_array_of_multiple_numbers():
    # arrange
    numbers = [4, 5, -8, 3, 11, -21, 6]
    expectedResult = 11
    cut = HighestNumberFinder()

    # act
    result = cut.find_highest_number(numbers)
    # assert

    assert expectedResult == result


def test_array_of_same_numbers():
    # arrange
    numbers = [46,46,46,46,7,6,5,4]
    expectedResult = 46
    cut = HighestNumberFinder()

    # act
    result = cut.find_highest_number(numbers)
    # assert

    assert expectedResult == result