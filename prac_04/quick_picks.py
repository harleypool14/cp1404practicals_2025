import random

NUMBER_PER_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


def main():
    quick_pick_count = int(input("How many quick picks? "))
    while quick_pick_count < 0:
        print("Invalid")
        quick_pick_count = int(input("How many quick picks? "))

