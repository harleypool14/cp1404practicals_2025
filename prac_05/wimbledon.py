"""
Emails
Estimate: 50 minutes
Actual:   minutes
"""

FILENAME = "wimbledon.csv"
COUNTRY = 1
CHAMPION = 2

def main():
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)

def get_records():
    return

def process_records():
    return

def display_results():
    return

if __name__ == '__main__':
