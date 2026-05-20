def rem_duplicate(tup):
    no_duplicate = []
    
    for item in tup:
        if item not in no_duplicate:
            no_duplicate.append(item)
            
    return tuple(no_duplicate)

# Function Call
print(rem_duplicate((1, 1, 1, 2, 3, 4, 5, 6, 6, 6, 6, 4, 0, 0, 0)))
print(rem_duplicate(("Hi", 1, 2, 3, 3, "Hi", 'a', 'a', [1, 2])))