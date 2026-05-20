N = int(input("Input: "))
total = 0

for counter in range(1, N + 1):
    if counter % 7 == 0:
        total += counter
print(total)