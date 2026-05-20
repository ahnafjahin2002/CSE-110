str_input = input("Input: ")

if len(str_input) == 0:
    print(str_input)
else:
    new_str = str_input[0]
    for i in range(1, len(str_input)):
        if str_input[i] != str_input[i - 1]:
            new_str += str_input[i]
            
    print(new_str)