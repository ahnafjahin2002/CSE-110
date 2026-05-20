import math

def area_circumference_generator(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    return (area, circumference)

# Function Call with tuple unpacking
area, circumference = area_circumference_generator(1)
print(area_circumference_generator(1))
print(f"Area of the circle is {area} and circumference is {circumference}")