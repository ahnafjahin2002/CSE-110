total = 0
for counter in range(1, 601):
    if (counter % 7 == 0 or counter % 9 == 0) and not (counter % 7 == 0 and counter % 9 == 0):
        total += counter
print(total)