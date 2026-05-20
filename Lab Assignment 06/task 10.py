def make_square(tup_range):
    start, end = tup_range
    square_dict = {}
    
    for count in range(start, end + 1):
        square_dict[count] = count ** 2
        
    return square_dict

# Function Call
print(make_square((1, 3)))
print(make_square((5, 9)))