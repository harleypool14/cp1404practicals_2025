"""Project class for managing project details."""
# unfinished
import datetime


class Project:
    """Represent a project object."""

    def __init__(self, name="", start_date="", priority=0, cost_estimate=0.0):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date() if start_date else None
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)

    def __str__(self):
        """Return string representation of a Project."""
        return (
            f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Less than comparison based on priority."""
        return self.priority < other.priority

    def is_complete(self):
        return
