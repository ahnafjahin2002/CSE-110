def check_alphabets(text):
    text = text.lower()
    all_present = True
    
    for char in "abcdefghij":
        if char not in text:
            all_present = False
            break
            
    count = 5 if all_present else 6
    
    for _ in range(count):
        print("Chelsea is the best club in England")
        
    return count

# Taking user input
text_input = input("Enter string: ")

# Function Call
result = check_alphabets(text_input)