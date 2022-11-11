"""Examples of 'vectorized' operations via magic methods."""

from __future__ import annotations
from typing import Union

class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"
    
    def __add__(self, rhs: str) -> StrArray:
        result: StrArray = StrArray([])
        # 1. Loop through every item in self's items list
        if isinstance(rhs, str):
            for i in self.items:
                result.items.append(i + rhs)
        else:
            for i in range(len(self.items)):
                result.items.append(self.items[i] + rhs.items[i])
        return result


a: StrArray = StrArray(["Armando", "Pete", "Leaky"])
b: StrArray = StrArray(["Bacot", "Nance", "Black"])
print(a + "!")
print(a + " " + b)
print(b + ", " + a + "!")