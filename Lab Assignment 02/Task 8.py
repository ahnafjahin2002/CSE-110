total = 0
count = 0

for i in range(10):
    num = int(input("Input: "))
    if num % 2 != 0:
        total += num
        count += 1

average = total / count
print(f"Total is {total} and Average is {average}")