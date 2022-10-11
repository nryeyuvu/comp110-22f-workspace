"""Unit tests to functions in ex07_dictionary."""

__author__ = "730552319"


from exercises.ex07.dictionary import invert, favorite_color, count


# Unit tests for invert
def test_invert_empty() -> None:
    """Edge case for invert."""
    key: dict[str, str] = {}
    assert invert(key) == {}


def test_invert_one() -> None:
    """Use case with only one key and value."""
    key: dict[str, str] = {'Tree': 'Leaf'}
    assert invert(key) == {'Leaf': 'Tree'}


def test_invert_multiple() -> None:
    """Use case with only multiple keys and values."""
    key: dict[str, str] = {'Class1': 'IDST 118', 'Class2': 'COMP 110', 'Class3': 'ENGL 105'}
    assert invert(key) == {'IDST 118': 'Class1', 'COMP 110': 'Class2', 'ENGL 105i': 'Class3'}


# Unit tests for favorite_color
def test_favorite_color_empty() -> None:
    """Edge case for favorite_color."""
    key: dict[str, str] = {}
    assert invert(key) == ''


def test_favorite_color_normal() -> None:
    """Use case for normal cases for favorite_color."""
    key: dict[str, str] = {"James": "red", "Max": "blue", "Jessi": "blue"}
    assert invert(key) == 'blue'


def test_favorite_color_order() -> None:
    """Use case testing to give right output even when two colors have same count."""
    key: dict[str, str] = {"James": "red", "Max": "red", "Jessi": "blue", "Naga": "blue"}
    assert invert(key) == 'red'


# Unit tests for count
def test_count_empty() -> None:
    """Edge case for count."""
    inputted_list: list[str] = []
    assert count(inputted_list) == {}


def test_count_one_element() -> None:
    """Use case for count."""
    inputted_list: list[str] = ["key"]
    assert count(inputted_list) == {"key": 1,}

def test_count_two_elements() -> None:
    """Second use case for count."""
    inputted_list: list[str] = ["key", "key"]
    assert count(inputted_list) == {"key": 2}