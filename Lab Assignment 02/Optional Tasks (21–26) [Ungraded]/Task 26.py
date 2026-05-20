start = int(input("Start: "))
end = int(input("End: "))

prime_count = 0
perfect_count = 0
prime_str = "Prime numbers: "
perfect_str = "Perfect numbers: "

for num in range(start, end + 1):
    
    # Check Prime
    is_prime = True
    if num < 2:
        is_prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
    
    if is_prime:
        prime_count += 1
        prime_str += str(num) + " "
        
    # Check Perfect
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
            
    if sum_divisors == num and num > 0:
        perfect_count += 1
        perfect_str += str(num) + " "

print(f"Between {start} and {end},")
print(f"Found {prime_count} prime numbers")
print(f"Found {perfect_count} perfect number")
print(prime_str)
print(perfect_str)