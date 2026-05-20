word = input("Input: ")

if len(word) < 4:
    print(word)
elif word.endswith("er"):
    print(word[:-2] + "est")
elif word.endswith("est"):
    print(word)
else:
    print(word + "er")