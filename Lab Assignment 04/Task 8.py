list_one = [int(count) for count in input("List_one : ").strip("[]").split(",")]
list_two = [int(count) for count in input("List_two : ").strip("[]").split(",")]

has_common = False
for item in list_one:
    if item in list_two:
        has_common = True
        break
        
print(has_common)