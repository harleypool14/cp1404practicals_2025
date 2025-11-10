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


def load_guitars():
    return


def save_guitars():
    return


def get_new_guitar():
    return


def display_guitars():
    return


if __name__ == '__main__':
    main()
