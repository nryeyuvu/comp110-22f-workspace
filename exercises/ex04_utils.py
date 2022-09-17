"""Utilizing pythons preferred functions and idioms."""

__author__ = "730552319"

def all(l: list[int], i: int) -> bool:
    """Checks to see if all the integers in a list match a set integer"""
    count: int = 0
    check: bool = False
    while count < len(l):
        if l[count] == i:
            check = True
        else:
            check = False
        count += 1
    return check

def max(inputted_list: list[int]) -> int:
    """Finds the highest number in a list of integers."""
    if len(inputted_list) == 0:
        raise ValueError("max() arg is an empty List")
        return
    i: int = 1
    max_value: int = inputted_list[0]
    while i < len(inputted_list):
        if inputted_list[i - 1] > inputted_list[i]:
            max_value = inputted_list[i - 1]
        elif inputted_list[i - 1] < inputted_list[i]:
            max_value = inputted_list[i]
        i += 1
    return max_value

def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks to see if two lists are equal to each other"""
    index: int = 0
    if len(list1) != len(list2):
        return False
    while index < len(list1):
        if list1[index] != list2[index]:
            return False
        index += 1
    return True