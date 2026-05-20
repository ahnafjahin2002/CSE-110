N = int(input("Input: "))

fib1 = 0
fib2 = 1

if N >= 0:
    print(fib1, end=" ")
if N >= 1:
    print(fib2, end=" ")

next_fib = fib1 + fib2
while next_fib <= N:
    print(next_fib, end=" ")
    fib1 = fib2
    fib2 = next_fib
    next_fib = fib1 + fib2
print()