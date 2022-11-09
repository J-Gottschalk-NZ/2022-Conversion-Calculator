my_dict = {
    "blue": "sky",
    "green": "grass",
    "yellow": "sun",
    "red": "apple"
}

# list to make testing faster.  
to_check = ["blue", "sky", "apple", "salad"]

for item in to_check:
    
    # check if it's a key (ie: a colour in our dictionary)
    if item in my_dict:
        print("{} is a key in the dictionary".format(item))
        
        # look up the value associated with the key
        coloured_object = my_dict[item]
        
        # output the value and the key (eg: the sky is blue)
        print("The {} is {}".format(coloured_object, item))
        
    # check if it's a value (ie: an object in our dictionary)
    elif item in my_dict.values():
        print("{} is a value in the dictionary".format(item))
    
    # if it's not anywhere in the dictionary (ie: is not a key or a value)    
    # tell the user it's not there.
    else:
        print("{} is not in the dictionary".format(item))
        
    print()