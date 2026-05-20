list_one = [int(count) for count in input("List_one : ").strip("[]").split(",")]
list_two = [int(count) for count in input("List_two : ").strip("[]").split(",")]

# Take everything in list_one except the last element, and add list_two
new_list = list_one[:-1] + list_two
print(new_list)