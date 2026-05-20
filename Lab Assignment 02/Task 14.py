number = int(input("Input: "))
count = 0

for div in range(1, number + 1):
    if number % div == 0:
        if div == number:
            print(div)
        else:
            print(div, end=", ")
        count += 1
print("Total", count, "divisors.")