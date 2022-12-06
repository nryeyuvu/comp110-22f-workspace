
def reverse_multiply(original: list[int]) ->list[int]:
    i: int = len(original) - 1
    new_list: list[int] = []
    while i > 0:
        new_list.append(original[i] * 2)
        i -= 1
    return new_list


def free_biscuits(games: dict[str, list[int]]) -> dict[str, bool]:
    new_return: dict[str, bool] = {}

    for i in games:
        total_points: int = 0
        for j in games[i]:
            total_points += j
        
        if total_points >= 100:
            new_return[i] = True
        else:
            new_return[i] = False
    return new_return


def multiples(num: list[int]) -> list[bool]:
    i: int = 1
    new_list: list[bool] = []

    if num[0] % num[len(num) - 1] == 0:
        new_list.append(True)
    else:
        new_list.append(False)

    while i < len(num):
        if num[i] % num[i - 1] == 0:
            new_list.append(True)
        else:
            new_list.append(False)
        i += 1
    return new_list


def merge_lists(string_merge: list[str], int_merge: list[int]) -> dict[str, int]:
    new_dict: dict[int, str] = {}
    i: int = 0
    if len(string_merge) != len(int_merge):
        return new_dict

    while i < len(string_merge):
        new_dict[string_merge[i]] = int_merge[i]
        i += 1
    
    return new_dict

def reverse_string(word: str) -> str:
    new_word: str = ""
    i: int = 0
    while i < len(word):
        new_word += word[len(word) - 1 - i]
        i += 1
    return new_word

    
# Recursion coding practice
def factorial(start: int) -> int:
    if start <= 2:
        return start
    else:
        return start * factorial(start - 1)