dictionary = {'a': 6, 'b': 7, 'c': 9, 'd': 8, 'e': 11, 'f': 12, 'g': 13}

lower = int(input("Lower bound (inclusive): "))
upper = int(input("Upper bound (exclusive): "))

new_dict = {}

for key, value in dictionary.items():
    if lower <= value < upper:
        new_dict[key] = value
        
print(new_dict)