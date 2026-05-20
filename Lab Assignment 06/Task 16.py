def splitting_money(amount):
    notes = [500, 100, 50, 20, 10, 5, 2, 1]
    result = ""
    
    for note in notes:
        if amount >= note:
            count = amount // note
            amount = amount % note
            result += f"{note} Taka: {count} note(s)\n"
            
    return result.strip()

# Taking user input
amount_input = int(input("Enter amount: "))

# Function Call
print(splitting_money(amount_input))