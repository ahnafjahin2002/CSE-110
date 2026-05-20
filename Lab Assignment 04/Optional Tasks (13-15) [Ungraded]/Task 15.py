user_input = input("Please input numbers separated by comma: ")
my_list = [int(element) for element in user_input.split(",")]

# Find the absolute largest first
largest = my_list[0]
for num in my_list:
    if num > largest:
        largest = num

# Set initial second largest to an infinitely small number
# Ensure it doesn't match the largest number
second_largest = -float('inf')
second_idx = -1

for i in range(len(my_list)):
    if my_list[i] > second_largest and my_list[i] < largest:
        second_largest = my_list[i]
        second_idx = i

print(f"My list: {my_list}")
print(f"Second largest number in the list is {second_largest} which was found at index {second_idx}.")