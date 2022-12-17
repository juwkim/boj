N = int(input())
for i in range(1, N - 4, 6):
    print(*range(i, i + 6), 'Go!', end=' ')
if N % 6:
    print(*range(N - N % 6 + 1, N + 1), 'Go!')