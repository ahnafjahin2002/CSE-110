user_input = input("Input: ").strip("[]")
user_list = [int(item) for item in user_input.split(",")]

squared_list = [item**2 for item in user_list]
print(squared_list)