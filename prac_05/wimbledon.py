"""
Emails
Estimate: 50 minutes
Actual: 42 minutes
"""

FILENAME = "wimbledon.csv"
COUNTRY = 1
CHAMPION = 2


def main():
    """Run the Wimbledon data program."""
    records = get_records(FILENAME)
    champion_count, countries = process_records(records)
    display_results(champion_count, countries)


def process_records(records):
    """Count champions and collect winning countries."""
    champion_count = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY])
    try:
        champion_count[record[CHAMPION]] += 1
    except KeyError:
        champion_count[record[CHAMPION]] = 1
    return champion_count, countries


def display_results(champion_to_count, countries):
    """Displays champions and countries."""
    print("Wimbledon Champions:")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def get_records(filename):
    """Read records from the CSV file."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove header
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()
