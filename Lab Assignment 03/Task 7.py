str_input = input("String Input: ")
index = int(input("Index Input: "))

# Reverse the prefix and concatenate with the unchanged suffix
part_1 = str_input[:index + 1][::-1]
part_2 = str_input[index + 1:]

print(part_1 + part_2)