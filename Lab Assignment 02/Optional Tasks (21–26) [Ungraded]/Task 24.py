even_sum = 0
even_count = 0
min_even = None

for i in range(5):
    num = int(input("Input: "))
    
    if num % 2 == 0:
        even_sum += num
        even_count += 1
        
        if min_even is None or num < min_even:
            min_even = num

if even_count > 0:
    print("Minimum", min_even)
    print("Average is", even_sum / even_count)