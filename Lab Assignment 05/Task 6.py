given_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

# Convert to list, reverse it, and convert back to tuple
temp_list = list(given_tuple)
temp_list.reverse()
reversed_tuple = tuple(temp_list)

print(reversed_tuple)