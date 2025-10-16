COLOUR_CODES = {"aliceblue": "#f0f8ff", "absolutezero": "#0048ba", "darkorchid": "#9932cc", "forestgreen": "#228b22",
                "goldenrod": "#daa520", "lavender": "#e6e6fa", "maroon": "#800000", "navy": "#000080",
                "plum": "#dda0dd", "amber": "#ffbf00"}

# Ask the user for a colour name and display its code
colour = input("Enter a colour name: ").lower()
while colour != "":
    print(f"The code for {colour} is {COLOUR_CODES.get(colour)}")
    colour = input("Enter a colour name: ").lower()
