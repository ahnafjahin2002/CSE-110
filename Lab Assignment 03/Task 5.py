str_1 = input("Input 1: ")
str_2 = input("Input 2: ")
result = ""

min_len = min(len(str_1), len(str_2))

for i in range(min_len):
    result += str_1[i] + str_2[i]

# Append the leftovers of whichever string is longer
result += str_1[min_len:] + str_2[min_len:]

print(result)