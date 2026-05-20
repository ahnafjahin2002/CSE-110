n = int(input("Input: "))
total = 0

for count in range(1, n + 1):
    if count % 2 != 0:
        total += (count ** 2)
    else:
        total -= (count ** 2)
print(total)