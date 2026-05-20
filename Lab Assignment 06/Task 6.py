def day_calc(total_days):
    years = total_days // 365
    remaining_days = total_days % 365
    
    months = remaining_days // 30
    days = remaining_days % 30
    
    print(f"{years} years, {months} months and {days} days")

# Taking user input
days_input = int(input("Enter days: "))    

# Function Call
day_calc(days_input)