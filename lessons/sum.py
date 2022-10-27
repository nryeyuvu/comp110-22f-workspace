"""Example of writing a test subject."""


def sum(xs: list[float]) -> float:
    """Count the sum of a list."""
    total: float = 0.0
    for x in xs:
        total += x
    return total
