all_units = {
    "mm": ["milimeters", "mms"],
    "cm": ["centimeters"],
    "h": ["hour", "hours", "hr", "hrs"],
    "min": ["minutes", "mins"]
}

test_data = ["mms", "cm", "mins"]


for entry in test_data:
    
    # if the unit is a key, return it
    if entry in all_units:
        valid_unit = entry
        
    
    # find input if it is anywhere in the dictionary
    for item in all_units:
        unit_list = all_units[item]
        
        if entry in unit_list:
            valid_unit = item
            done = "yes"
            break

    print(valid_unit)