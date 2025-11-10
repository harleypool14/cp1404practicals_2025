from guitar import Guitar


def main():
    filename = 'guitars.csv'
    guitars = load_guitars(filename)
    print("Loaded guitars:")
    display_guitars(guitars)

    print("\nSorted by year:")
    guitars.sort()
    display_guitars(guitars)

    print("\nAdd new guitars:")
    name = input("Name: ")
    while name != "":
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
            print(f"{guitar.name} has been added.")
        except ValueError:
            print("Invalid input. Please enter valid numbers for year and cost.")
        name = input("Name: ")

    save_guitars(guitars, filename)
    print("\nGuitars have been saved to", filename)
    print("\nFinal guitar collection:")
    display_guitars(guitars)


def load_guitars(filename):
    guitars = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, year, cost = line.strip().split(',')
                guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty guitar list.")
    return guitars


def save_guitars(guitars, filename):
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def get_new_guitar():
    return


def display_guitars():
    return


if __name__ == '__main__':
    main()
