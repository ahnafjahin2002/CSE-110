def fibonacci(limit):
    if limit < 0:
        print("Wrong Input: Limit cannot be a negative number! Please run the program again.")
        return
    
    a, b = 0, 1
    while a <= limit:
        print(a, end=" ")
        a, b = b, a + b
    print() # To add a newline after the sequence

# Function Call        
fibonacci(10)
fibonacci(5)