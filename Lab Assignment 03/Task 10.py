str_input = input("Input: ")
result = ""

for i in range(len(str_input)):
    # Keep characters that are on odd indices
    if i % 2 != 0:
        result += str_input[i].upper()

print(result)