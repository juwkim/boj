N = int(input())
for i in range(N, 0, -1):
    print(("*" * (2 * i - 1) + ' ').rjust(i + N))