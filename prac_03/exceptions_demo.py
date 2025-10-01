"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur when a function receives an argument of the correct data type
but an inappropriate value.
2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur when a number is attempted to be divided by zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes you can add a while loop so that if the denominator is 0 it keeps asking until
there is a valid input that is not zero.
"""


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
