"""
Emails
Estimate: 25 minutes
Actual:    minutes
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        confirm = input(f"Is your name {name}? (Y/n) ").lower()
        if confirm.upper() != "Y" and confirm != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")


main()
