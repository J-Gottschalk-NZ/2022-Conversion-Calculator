def unit_checker(possible_lists):
    
    invalid_holder = []
       
    while True:
        from_unit = input("Enter the unit you have: ")
        
        for item in possible_lists:
        
            if from_unit in item:
                to_unit = input("Enter the unit you want to convert into: ")
                
                if to_unit in item:
                    return [from_unit, to_unit]
                
            else:
                invalid_holder.append(item)
                
        if len(invalid_holder) == len(possible_lists):
            print("Please enter a valid unit to convert from")
        else:
            print("Please try again, it is not possible to convert between {} and {}".format(to_unit, from_unit))
                
                


# *** Main Routine Goes here ****

# *** Units Dictionaries ****

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

# List of dictionaries for use in unit checker
all_dicts = [distance, time]

get_units = unit_checker(all_dicts)
print(get_units)