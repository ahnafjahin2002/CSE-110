user_input = input("Input: ")
# Split by comma, strip whitespace, then strip the quotes
raw_list = [item.strip().strip("\"'") for item in user_input.split(",")]

clean_list = [item for item in raw_list if item != ""]
print(clean_list)