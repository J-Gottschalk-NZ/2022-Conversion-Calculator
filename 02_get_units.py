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

all_units = distance | time

unit = input("input a unit: ")
if unit in all_units:
    print("it's valid")
else:
    print("its not valid")