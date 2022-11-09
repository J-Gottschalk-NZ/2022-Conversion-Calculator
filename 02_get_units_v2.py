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

# use list so we don't have to keep inputting test data
to_test = ["cm", "min", "salad"]

for unit in to_test:
    if unit in all_units:
        print("{} is a valid unit".format(unit))
    else:
        print("{} is not a valid unit".format(unit))