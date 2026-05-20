
dict_1 = {'Harry': 15, 'Draco': 8, 'Nevil': 19}
dict_2 = {'Ginie': 18, 'Luna': 14}

# Using the dictionary unpacking operator to merge
marks = {**dict_1, **dict_2}

print(marks)