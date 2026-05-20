given_dict = {'A': [1, 2, 3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
total_items = 0

for val_list in given_dict.values():
    for item in val_list:
        total_items += 1
        
print(total_items)