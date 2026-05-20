def remove_odd(mixed_list):
    even_list = [num for num in mixed_list if num % 2 == 0]
    return even_list

# Function Call
print(remove_odd([21, 33, 44, 66, 11, 1, 88, 45, 10, 9]))
print(remove_odd([11, 2, 3, 4, 5, 2, 0, 5, 3]))