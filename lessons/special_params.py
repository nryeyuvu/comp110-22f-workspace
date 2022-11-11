"""Examples of optional parameters and Union types."""

from typing import Union

def hello(name: Union[str, int] = "World") -> str:
    """A delightful greeting."""
    greeting: str = "Hello, " + name
    if isinstance(name, str):
        greeting += name
    elif isinstance(name, int):
        greeting += "COMP" + str(name)
    else:
        greeting += "Alien Lifefrom Sector" + str(name)
    return greeting


# Single-argument
print(hello("Sally"))

# No arguments!
print(hello())

# int argument works too!
print(hello(110))
print(hello(3.14))
