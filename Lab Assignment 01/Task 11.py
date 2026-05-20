student_mark = int(input("Please Enter the student's mark: "))

if (90 <= student_mark <= 100):
    print("A")
elif (80 <= student_mark <= 89):
    print("B")
elif (70 <= student_mark <= 79):
    print("C")
elif (60 <= student_mark <= 69):
    print("D")
elif (50 <= student_mark <= 59):
    print("E")
elif (0 <= student_mark < 50):
    print("F")
else:
    print("Error: Please enter Student marks in the range between 0 to 100")