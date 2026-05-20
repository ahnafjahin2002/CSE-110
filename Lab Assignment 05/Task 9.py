exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
threshold = int(input("Input: "))

new_marks = {}

for key, value in exam_marks.items():
    if value >= threshold:
        new_marks[key] = value
        
print(new_marks)