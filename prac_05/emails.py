"""
Emails
Estimate: 25 minutes
Actual:  32  minutes
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ").lower()
        if confirm.upper() != "Y" and confirm != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
