def first_unit(valid_options):
    
    while True:
        response = input("Enter the unit you have: ")
        if response in valid_options:
            return response
        else:
            print("Please enter a valid unit")

distance = {
    "mm": 1000,
    "cm": 100,
    "m" : 1,
    "km": 0.001
}

time = {
    "s": 3600,
    "min": 60,
    "hour": 1
}


# We can combine dictionaries using '|' (needs Python 3.9 and higher)
all_units = distance | time

given_unit = first_unit(all_units)
print("You chose {}".format(given_unit))