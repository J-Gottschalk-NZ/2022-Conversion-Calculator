# checks user has entered a number that is more than zero
def num_check(question):
    valid = False
    while not valid:
        
        error = "Please enter a number that is more than zero"
        
        try:
        
            # ask user to enter a number
            response = float(input(question))
            
            # checks number is more than 0
            if response > 0:
                return response
            
            # outputs error if input is invalid
            else:
                print(error)
                print()
                
        except ValueError:
            print(error)    
    
    
def units_abbreviations(question):
    
    # list of posssible units, function will return first item in a given list
    possible_units = [
        ["mm", "milimeters", "milimetres"],
        ["cm", "centimeters", "centimetres", "cms"], 
        ["m", "meters", "metres"],
        ["km", "kilometers", "kilometres"],
        ["s", "seconds", "secs", "second", "sec"],
        ["min", "mins", "minutes"],
        ["hrs", "h", "hour", "hours", "hr"]
    ]
    
    while True:
        response = input(question)
        
        for item in possible_units:
            if response in item:
                return item[0]
            
        else:
            print("Sorry - that unit is not valid / supported by this program")
    
# checks user has entered valid units (ie: can't choose cm and hrs)
def unit_checker(possible_lists):
    
    # possible units lists...
    
    
    invalid_holder = []
       
    while True:
        from_unit = units_abbreviations("Enter the unit you have: ")
        
        for item in possible_lists:
        
            if from_unit in item:
                to_unit = units_abbreviations("Enter the unit you want to convert into: ")
                
                if to_unit in item:
                    return [from_unit, to_unit]
                
            else:
                invalid_holder.append(item)
                
        if len(invalid_holder) <= len(possible_lists):
            print("Please enter a valid unit to convert from")
        else:
            print("Please try again, it is not possible to convert between {} and {}".format(to_unit, from_unit))


# if float ends in .0, changes it to an integer
def display_int(var_int):
        if var_int % 1 == 0:
            return int(var_int)
        else: return (var_int)

# Main Routine goes here

# Ask user if they wnat to see the instructions

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
"hrs": 1
}

# combines all the dictionaries so that we can look up conversion factors in one place
combined_units = distance | time

# List of dictionaries for use in unit checker
all_dicts = [distance, time]

keep_going = ""
while keep_going == "":
    print("going")
        
    # ask user to enter amount
    amount = num_check("Enter the amount you want to convert: ")

    # ask user for units (what they have and what they want)
    # function checks that units are valid
    get_units = unit_checker(all_dicts)
    convert_from = get_units[0]
    convert_to = get_units[1]
    print("You have chosen to convert from {} to {}".format(convert_from, convert_to))

    # Do conversion
    to_standard = amount * combined_units[convert_to]
    converted = to_standard / combined_units[convert_from]
    
    # display whole number results as an integer
    amount = display_int(amount)
    converted = display_int(converted)  
    
    # Output result
    
    print()
    print("{} {} is {} {}".format(amount, convert_from, converted, convert_to))
    
    print()
    keep_going = input("Press <enter> for another calculation or any key to quit")
    print()