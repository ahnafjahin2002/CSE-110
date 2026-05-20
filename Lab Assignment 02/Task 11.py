number = int(input("Input: "))
str_number = str(number)

for i in range(len(str_number)):
    if i == len(str_number) - 1:
        print(str_number[i], end="")
    else:
        print(str_number[i], end=", ")
        