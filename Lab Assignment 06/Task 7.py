def show_palindrome(num):
    result = ""
    # Loop for the ascending part
    for i in range(1, num + 1):
        result += str(i)
    # Loop for the descending part
    for i in range(num - 1, 0, -1):
        result += str(i)
        
    return result

# Function Call
print(show_palindrome(5))
print(show_palindrome(3))