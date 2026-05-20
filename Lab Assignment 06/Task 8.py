
def show_palindrome(num):
    result = ""
    for i in range(1, num + 1):
        result += str(i)
    for i in range(num - 1, 0, -1):
        result += str(i)
    return result


def show_palindromic_triangle(num):
    for i in range(1, num + 1):
        # Print spaces for alignment
        for space in range(num - i):
            print(" ", end=" ")
            
        # Get the palindrome string from the helper function and print it with spaces
        pal_string = show_palindrome(i)
        for char in pal_string:
            print(char, end=" ")
        
        # Newline after each row
        print()

# Function Call
show_palindromic_triangle(5)