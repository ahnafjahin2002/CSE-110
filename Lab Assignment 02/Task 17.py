quantity = int(input("Quantity: "))

total = 0
max_val = None
min_val = None

for i in range(quantity):
    num = int(input("Number: "))
    total += num
    
    if max_val is None or num > max_val:
        max_val = num
    if min_val is None or num < min_val:
        min_val = num

print("Maximum", max_val)
print("Minimum", min_val)
print("Average is", total / quantity)