user_input = input("String Input: ")
split_char = input("Split Character: ")

word = ""
for ch in user_input:
    if ch == split_char:
        print(word)
        word = ""
    else:
        word += ch
print(word) # Prints the final word