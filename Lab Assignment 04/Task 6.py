user_input = input("Please input 5 numbers separated by comma: ")
my_list = [int(element) for element in user_input.split(",")]

num_large = my_list[0]
large_index = 0

for i in range(len(my_list)):
    if my_list[i] >= num_large:
        num_large = my_list[i]
        large_index = i

print(f"My list: {my_list}")
print(f"Largest number in the list is {num_large} which was found at index {large_index}.")