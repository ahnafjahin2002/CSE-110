def sum_exclusive_divisors(start, end, div_1, div_2):
    total_sum = 0
    
    for i in range(start, end):
        # Divisible by one or the other, but not both
        if (i % div_1 == 0 or i % div_2 == 0) and not (i % div_1 == 0 and i % div_2 == 0):
            total_sum += i
            
    return total_sum

# Taking user input
start = int(input("Start: "))
end = int(input("End: "))
div_1 = int(input("Divisor 1: "))
div_2 = int(input("Divisor 2: "))

# Function Call
print(sum_exclusive_divisors(start, end, div_1, div_2))