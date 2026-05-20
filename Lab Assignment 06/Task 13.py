def basic_calc(operator, num_1, num_2):
    if operator == "+":
        return num_1 + num_2
    elif operator == "-":
        return num_1 - num_2
    elif operator == "/":
        return num_1 / num_2
    elif operator == "*":
        return num_1 * num_2

# Taking user input
operator = input("Operator: ")
num_1 = float(input("First Operand: "))
num_2 = float(input("Second Operand: "))

# Function Call
print(basic_calc(operator, num_1, num_2))