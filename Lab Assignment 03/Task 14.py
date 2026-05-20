str_1 = input("Input 1: ")
str_2 = input("Input 2: ")

# Sorting both strings guarantees that if they have the exact same letters, they will match.
if sorted(str_1) == sorted(str_2):
    print("They are anagram")
else:
    print("They are not anagram")