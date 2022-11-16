"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730552319"


class Simpy:
    """Helps with working with sequences."""
    values: list[float]

    def __init__(self, values: list[float]) -> None:
        """Constructor."""
        self.values = values
    
    def __repr__(self) -> str:
        """Special method to represent object as string."""
        convert: str = "Simpy(["
        i: int = 0
        while i < len(self.values):
            if i == len(self.values) - 1:
                convert += str(self.values[i]) + "])"
            else:
                convert += str(self.values[i]) + ", "
            i += 1
        return convert

    def fill(self, fill_value: float, num_values: int) -> None:
        """Fills empty list with 'fill_value' 'num_value' amount of times."""
        for i in range(len(self.values)):
            self.values.pop()
        while num_values > 0:
            self.values.append(fill_value)
            num_values -= 1

    # Why neg nums not working
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attribute with range of values."""
        assert step != 0.0
        i: int = 0
        fill: float = 0
        while fill != (stop - step):
            fill = start + (step * i)
            self.values.append(fill)
            i += 1

    def sum(self) -> float:
        """Sums all the elements in 'values'."""
        num: float = 0.0
        for i in self.values:
            num += i
        return num   

    def __add__(self, b: Union[Simpy, float]) -> Simpy:
        """Adds either another 'Simpy' or float to list of values."""
        unmutate: Simpy = Simpy([])
        if isinstance(b, float):
            for i in self.values:
                unmutate.values.append(i + b)
        else:
            assert len(self.values) == len(b.values)
            for i in range(len(self.values)):
                unmutate.values.append(self.values[i] + b.values[i])
        return unmutate

    def __pow__(self, b: Union[Simpy, float]) -> Simpy:
        """Exponentiation either another 'Simpy' or float to list of values."""
        unmutate: Simpy = Simpy([])
        if isinstance(b, float):
            for i in self.values:
                unmutate.values.append(i ** b)
        else:
            assert len(self.values) == len(b.values)
            for i in range(len(self.values)):
                unmutate.values.append(self.values[i] ** b.values[i])
        return unmutate
    
    def __eq__(self, b: Union[float, Simpy]) -> list[bool]:
        """Test equality of each item in the 'values' attribute."""
        unmutate: list[bool] = []
        if isinstance(b, float):
            for i in self.values:
                if i == b:
                    unmutate.append(True)
                else:
                    unmutate.append(False)
        else:
            assert len(self.values) == len(b.values)
            for i in range(len(self.values)):
                if self.values[i] == b.values[i]:
                    unmutate.append(True)
                else:
                    unmutate.append(False)
        return unmutate
    
    def __gt__(self, b: Union[float, Simpy]) -> list[bool]:
        """Test > of each item in the 'values' attribute."""
        unmutate: list[bool] = []
        if isinstance(b, float):
            for i in self.values:
                if i > b:
                    unmutate.append(True)
                else:
                    unmutate.append(False)
        else:
            assert len(self.values) == len(b.values)
            for i in range(len(self.values)):
                if self.values[i] > b.values[i]:
                    unmutate.append(True)
                else:
                    unmutate.append(False)
        return unmutate
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overload the subscription notation."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            unmutate = Simpy([])
            for i in range(len(self.values)):
                if rhs[i]:
                    unmutate.values.append(self.values[i])
                i += 1
        return unmutate