"""Unit tests to functions in ex05_utils."""

__author__ = "730552319"


from exercises.ex05.utils import only_evens, sub, concat


# Unit tests for only_evens
def test_only_evens_empty() -> None:
    """Edge case for only_evens."""
    inputted_list: list[int] = []
    assert only_evens(inputted_list) == []


def test_only_evens_oneResult() -> None:
    """One use case returning only on input."""
    inputted_list: list[int] = [1, 2, 3]
    assert only_evens(inputted_list) == [2]


def test_only_evens_allResult() -> None:
    """Case where all elements are even."""
    inputted_list: list[int] = [6, 6, 6]
    assert only_evens(inputted_list) == [6, 6, 6]


# Unit tests for concat
def test_concat_empty() -> None:
    """Edge case for concat."""
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []


def test_concat_sameList() -> None:
    """Returns two identical lists concatenated."""
    list_1: list[int] = [1, 2, 3]
    list_2: list[int] = [1, 2, 3]
    assert concat(list_1, list_2) == [1, 2, 3, 1, 2, 3]


def test_concat_differentList() -> None:
    """Returns a concatenation of two different lists."""
    list_1: list[int] = [1, 4, 6]
    list_2: list[int] = [3, 2, 5]
    assert concat(list_1, list_2) == [1, 4, 6, 3, 2, 5]


# Unit tests for sub
def test_sub_empty() -> None:
    """Edge case for sub."""
    list: list[int] = []
    start_index: int = 0
    end_index: int = 0
    assert sub(list, start_index, end_index) == []


def test_sub_oneResult() -> None:
    """Use case for sub where only one value is returned."""
    list: list[int] = [5, 10, 15, 18]
    start_index: int = 0
    end_index: int = 1
    assert sub(list, start_index, end_index) == [5]


def test_sub_twoResult() -> None:
    """Use case for sub where two values are returned."""
    list: list[int] = [5, 10, 15, 18]
    start_index: int = 1
    end_index: int = 3
    assert sub(list, start_index, end_index) == [10, 15]