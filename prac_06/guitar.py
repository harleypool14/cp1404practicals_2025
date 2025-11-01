"""
estimate: 45 minutes
time taken:  minutes
"""

CURRENT_YEAR = 2025
VINTAGE_YEAR = 50


class Guitar:
    """Represent a guitar with a name, year, and cost."""
    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name}, {self.year}, ${self.cost:.2f}"

    def get_age(self):
        """Calculate and return guitar's age"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if guitar is vintage"""
        return self.get_age() >= VINTAGE_YEAR
