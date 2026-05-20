user_input = input("Please input 5 numbers separated by comma: ")
my_list = [int(element) for element in user_input.split(",")]

num_large = my_list[0]
num_small = my_list[0]
large_idx = 0
small_idx = 0

for i in range(len(my_list)):
    if my_list[i] > num_large:
        num_large = my_list[i]
        large_idx = i
    if my_list[i] < num_small:
        num_small = my_list[i]
        small_idx = i
        
print(f"My list: {my_list}")
print(f"Smallest number in the list is {num_small} which was found at index {small_idx}")
print(f"Largest number in the list is {num_large} which was found at index {large_idx}")