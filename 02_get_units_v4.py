def units_abbreviations(question):
    # list of possible units, function will return first item in a given list
    possible_units = [
        ["mm", "millimeters", "millimetres", "millimeter", "millimetre"],
        ["cm", "centimeters", "centimeter", "cms", "centimetres", "centimetre"],
        ["m", "meters", "metres", "meter", "metre"],
        ["km", "kilometers", "kilometres", "kilometer", "kilometre"],
        ["ms", "milliseconds", "millisecond"],
        ["s", "seconds", "secs", "second", "sec"],
        ["min", "mins", "minutes", "minute"],
        ["h", "hr", "hrs", "hour", "hours"],
        ["d", "days", "day"],
        ["y", "years", "year"]
    ]

    while True:
        response = input(question)

        for item in possible_units:
            if response in item:
                return item[0]

        else:
            print("Sorry - that unit is not valid / supported by this program")


# Main Routine starts here
distance = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": 0.001
}

time = {
    "ms": 3600 * 1000,
    "s": 3600,
    "min": 60,
    "h": 1,
    "d": 24,
    "y": 24 * 365 + 6 + 9/60    # accounts for leap years!
}

# We can combine dictionaries using '|' (needs Python 3.9 and higher)
all_units = distance | time

# use list so we don't have to keep inputting test data
while True:

    unit = units_abbreviations("Enter a unit: ")

    if unit in all_units:
        print(f"{unit} is a valid unit")
    else:
        print(f"Please enter a valid unit")
