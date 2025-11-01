"""
estimate: 35 minutes
time taken: 27 minutes
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""
    def __init__(self, name="", typing="", reflection="", year=""):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language uses dynamic typing."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing}, Typing, Reflection={self.reflection}, First appeard in {self.year}"


def run_tests():
    """Run test on programming language class"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print(python)
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
