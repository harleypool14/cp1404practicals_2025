"""
CP1404/CP5632 - Practical
Program to determine score status
"""


# score = float(input("Enter score: "))
# if score < 0 or score > 100:
#     print("Invalid score")
# elif score >= 90:
#     print("Excellent")
# elif score >= 50:
#     print("Passable")
# else:
#     print("Bad")


def main():
    MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    choice = ''
    score = ''
    while choice != 'Q':
        print(MENU)
        choice = input("Choice: ")
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            determine_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("farewell")
        else:
            print("Invalid")


def get_valid_score():
    score = float(input("Enter valid score: "))
    while score <= 0 or score >= 100:
        print("Invalid score")
        score = float(input("Enter valid score: "))
    return score


def determine_result(score):
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
    print(f"Your result is: {score:.0f}")


def show_stars(score):
    stars = '*' * int(score)
    print(f"Stars: {stars}")


main()

