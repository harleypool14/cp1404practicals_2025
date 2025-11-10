from guitar import Guitar


def main():
    """Main program for guitar collection management."""
    filename = 'guitars.csv'
    guitars = load_guitars(filename)
    print("Loaded guitars:")
    display_guitars(guitars)
    # Add the __lt__ method to the Guitar class for sorting by year
    Guitar.__lt__ = lambda self, other: self.year < other.year
    print("\nSorted by year:")
    guitars.sort()
    display_guitars(guitars)
    # Get new guitars from user
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
        # Save all guitars back to file
        save_guitars(guitars, filename)
        print("\nGuitars have been saved to", filename)
        print("\nFinal guitar collection:")
        display_guitars(guitars)


def load_guitars(filename):



def save_guitars(guitars, filename):



def get_new_guitar():



def display_guitars(guitars):

if __name__ == '__main__':
    main()
