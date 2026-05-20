user_input = input("Input: ").strip("[]")
user_list = [int(x) for x in user_input.split(",")]

if len(user_list) < 4:
    print("Not possible")
else:
    print(user_list[2:-2])