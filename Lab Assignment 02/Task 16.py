number = int(input("Input: "))
is_prime = True

if number < 2:
    is_prime = False
else:
    for div in range(2, number):
        if number % div == 0:
            is_prime = False
            break

if is_prime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")