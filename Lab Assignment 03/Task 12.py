str_input = input("String Input: ")
letter = input("Letter Input: ")

if letter in str_input:
    print(str_input.replace(letter, ""))
else:
    if len(str_input) > 3:
        print(str_input[1:-1])
    else:
        print(str_input)