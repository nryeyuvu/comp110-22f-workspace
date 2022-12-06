"""Class writing practice in 11/29 class."""

class Staff:
    name: str
    is_cs: bool

    def __init__(self, name: str, is_cs: bool) -> None:
        self.name = name
        self.is_cs = is_cs

    def greet(self) -> str:
        cs_text: str = ""
        if not self.is_cs:
            cs_text = "NOT "
        return f"Hello, I'm {self.name} {cs_text}in CS"
