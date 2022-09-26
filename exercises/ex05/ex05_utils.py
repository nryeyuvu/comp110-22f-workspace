"""Contains the functions that perform simple calculations."""

__author__ = "730552319"

def only_evens(inputted_list: list[int]) -> int:
    """Returns only the even elements in a list."""
    return_list: list[int] = []
    i: int = 0
    while i < len(inputted_list):
        if inputted_list[i] % 2 == 0:
            return_list.append(inputted_list[i])
        i += 1
    return return_list


def concat(list_1: list[int], list_2: list[int]) -> int:
    """Combines the elements of two different lists into one big list."""
    new_list: list[int] = []
    i: int = 0
    while i < len(list_1):
        new_list.append(list_1[i])
        i += 1
    j: int = 0
    while j < len(list_2):
        new_list.append(list_2[j])
        j += 1
    return new_list


def sub(list: list[int], start_index: int, end_index: int) -> int:
    """Returns a modified list from the specified start and end indexes."""
    if start_index < 0:
        start_index = 0
    elif end_index > len(list):
        end_index = len(list) - 1

    modified_list: list[int] = []
    i: int = start_index
    while i >= start_index and i < end_index:
        modified_list.append(list[i])
        i += 1
    return modified_list

