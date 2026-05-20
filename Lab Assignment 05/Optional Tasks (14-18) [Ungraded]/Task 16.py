my_dictionary = {'c1':'Red', 'c2':'Green', 'c3':None, 'd4':'Blue', 'a5':None}

# Dictionary comprehension to filter out None values
clean_dict = {k: v for k, v in my_dictionary.items() if v is not None}

print(clean_dict)