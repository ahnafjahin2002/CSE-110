def filter_list(a_list):
    new_list = []
    removed_count = 0
    
    for item in a_list:
        if new_list.count(item) < 2:
            new_list.append(item)
        else:
            removed_count += 1
            
    print(f"Removed: {removed_count}")
    return new_list

# Function Call
print(filter_list([1, 2, 3, 3, 3, 3, 4, 5, 8, 8]))
print(filter_list([10, 10, 15, 15, 20]))