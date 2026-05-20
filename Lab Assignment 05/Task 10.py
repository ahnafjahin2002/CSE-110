given_dict = {'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure': 14}

max_val = -1
max_key = ""

for key, value in given_dict.items():
    if value > max_val:
        max_val = value
        max_key = key
        
print(f"The highest selling book genre is '{max_key}' and the number of books sold are {max_val}.")