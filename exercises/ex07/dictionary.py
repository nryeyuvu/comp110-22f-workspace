"""Practice with some dictionary functions."""

__author__ = "730552319"


def invert(key: dict[str, str]) -> dict[str, str]:
    """Switches the keys and values."""
    new_dict: dict[str, str]
    new_dict = dict()
    for i in key:
        if key[i] in new_dict:
            raise KeyError
        new_dict[key[i]] = i
    return new_dict


def favorite_color(colors: dict[str, str]) -> str:
    """From a dictionary of two strings, returns color that was most 'liked'."""
    freq_of_colors: dict[str, int] = {}
    for i in colors:
        if colors[i] not in freq_of_colors:
            freq_of_colors[colors[i]] = 0
        else:
            freq_of_colors[colors[i]] += 1
    max: str = ""
    num: int = 0
    for k in freq_of_colors:
        if freq_of_colors[k] > num:
            num = freq_of_colors[k]
            max = k
    return max


def count(inputted_list: list[str]) -> dict[str, int]:
    """From a list of strings, determines the occurrence of each element in list."""
    freq_dict: dict[str, int] = {}
    for i in inputted_list:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    return freq_dict