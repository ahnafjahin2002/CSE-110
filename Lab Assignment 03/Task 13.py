str_input = input("Input: ")
result = ""
upper_next = True

for ch in str_input:
    if ch.isalpha():  # Check if it's a letter
        if upper_next:
            result += ch.upper()
            upper_next = False
        else:
            result += ch.lower()
            upper_next = True
    else:
        result += ch  # Append spaces and symbols as they are

print(result)