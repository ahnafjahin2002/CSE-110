list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_two = [10, 11, 12, -13, -14, -15, -16]

list_three = []
combined_list = list_one + list_two

for num in combined_list:
    if num % 2 == 0:
        list_three.append(num)

print(list_three)