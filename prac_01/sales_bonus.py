"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%
"""

LOW_BONUS = 0.1
HIGH_BONUS = 0.15
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus_amount = sales * LOW_BONUS
        print(f"{bonus_amount:.0f}")
    else:
        bonus_amount = sales * HIGH_BONUS
        print(f"{bonus_amount:.0f}")
    sales = float(input("Enter Sales: $"))

