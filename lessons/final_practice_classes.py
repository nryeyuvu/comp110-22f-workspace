"""Class writing practice for final."""

class TimeSpent:
    name: str
    purpose: str
    minutes: int

    def __init__ (self, name: str, purpose: str, minutes: int):
        self.name = name
        self.purpose = purpose
        self.minutes = minutes

    def add_time(self, time: int) -> None:
        self.minutes += time

    def reset(self) -> int:
        value: int = self.minutes
        self.minutes = 0
        return value

    def report(self) -> None:
        hours: int = self.minutes // 60
        minute: int = self.minutes % 60
        print(f"{self.name} has spent {hours} hours and {minute} minutes on {self.purpose}")


class HotCocoa:

    has_whip: bool
    flavor: str
    marshmallow_count: int
    sweetness: int

    def __init__(self, has_whip: bool, flavor: str, marshmallow_count: int, sweetness: int) -> None:
        self.has_whip = has_whip
        self.flavor = flavor
        self.marshmallow_count = marshmallow_count
        self.sweetness = sweetness

    def mallow_adder(self, mallows: int) -> None:
        self.marshmallow_count += mallows
        self.sweetness += (mallows * 2)

    def calorie_count(self) -> float:
        calories: int = 0
        if self.flavor == "vanilla" or self.flavor == "peppermint":
            calories += 30
        else:
            calories += 20

        if self.has_whip:
            calories += 100
        calories += (self.marshmallow_count / 2)

        return calories