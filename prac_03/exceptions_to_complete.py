"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

"""Prompts until user enters a valid integer and then prints it."""
is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print(f"Valid integer is: {result}")
