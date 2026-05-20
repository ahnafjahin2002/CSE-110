str_input = input("String Input: ")
num = int(input("Number Input: "))

if num % 2 == 0:
    print(str_input * (num * 2))
else:
    print(str_input * (num * 3))