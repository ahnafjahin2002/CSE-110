user_input = input("Input: ")

for ch in user_input:
    if ch == 'z':
        print('a', end="")
    else:
        print(chr(ord(ch) + 1), end="")
print() # to add a newline at the very end