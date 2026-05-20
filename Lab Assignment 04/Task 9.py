user_input = input("Enter 10 numbers separated by comma: ")
num_list = [int(num) for num in user_input.split(",")]

odd_list = [num for num in num_list if num % 2 != 0]
print(odd_list)