user_input = input("Input (M,N): ").split(',')
M = int(user_input[0])
N = int(user_input[1])

for row in range(M):
    for col in range(1, N + 1):
        print(col, end="")
    print()