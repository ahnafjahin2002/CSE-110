# Using eval() to safely and easily evaluate a dictionary string input like {'Jon': 100, 'Dan':200}
user_dict = eval(input("Enter dictionary: "))

total_sum = 0
count = 0

for value in user_dict.values():
    total_sum += value
    count += 1
    
if count > 0:
    average = total_sum / count
    print(f"Average is {average}.")