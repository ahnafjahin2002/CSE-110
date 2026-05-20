a_list = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
a_dict = {}

for key, value in a_list:
    if key in a_dict:
        a_dict[key].append(value)
    else:
        a_dict[key] = [value]
        
print(a_dict)