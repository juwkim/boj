N = int(input())
for i in range(N, 1, -1):
    print(('*' * (2 * i - 1) + ' ').rjust(N + i))
for i in range(N):
    print(('*' * (2 * i + 1) + ' ').rjust(N + i + 1))   