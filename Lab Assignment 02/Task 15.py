number = int(input("Input: "))
total_sum = 0

for div in range(1, number):
    if number % div == 0:
        total_sum += div
        
if total_sum == number:
    print(number, "is a perfect number")
else:
    print(number, "is not a perfect number")