number = int(input("Input: "))
binary = ""

if number == 0:
    binary = "0"

while number > 0:
    remainder = number % 2
    binary = str(remainder) + binary
    number = number // 2

print(binary)