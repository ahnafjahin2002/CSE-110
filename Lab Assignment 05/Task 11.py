user_input = input("Input: ").lower()
freq_dict = {}

for char in user_input:
    # Ignore spaces
    if char != " ":
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
            
print(freq_dict)