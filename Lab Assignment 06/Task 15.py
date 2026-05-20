def calculate_grocery(order_items, location="Dhanmondi"):
    price_dict = {"Rice": 105, "Potato": 20, "Chicken": 250, "Beef": 510, "Oil": 85}
    total = 0
    
    for item in order_items:
        if item in price_dict:
            total += price_dict[item]
            
    if location == "Dhanmondi":
        total += 30
    else:
        total += 70
        
    return total

# Function Call
print(calculate_grocery(["Rice", "Beef", "Rice"], "Mohakhali"))
print(calculate_grocery(["Rice", "Beef", "Rice"]))