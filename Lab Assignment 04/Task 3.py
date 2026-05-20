user_list = []

for count in range(5):
    user_input = int(input("Enter a number: "))
    user_list.append(user_input)

# Reverse and print
user_list.reverse()
for num in user_list:
    print(num)