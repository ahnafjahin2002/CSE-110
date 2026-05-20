number = int(input("Input: "))

while number > 0:
    digit = number % 10
    number = number // 10
    if number != 0:
        print(digit, end=", ")
    else:
        print(digit, end="")
        