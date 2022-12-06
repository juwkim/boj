N = int(input())
for i in range(N):
    print(("*" * (2 * i + 1) + ' ').rjust(i + N + 1))