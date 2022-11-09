my_dict = {
    "blue": "sky",
    "double": 2,
    "half": 0.5,
    "green": "grass",
    "yellow": "sun",
    "red": "apple"
}

your_num = int(input("Enter a number: "))
to_do = input ("double or half? ").lower()

# look up value
mulitply_by = my_dict[to_do]

# do math!
answer = your_num * mulitply_by
print("{} x {} = {}".format(your_num, mulitply_by, answer))