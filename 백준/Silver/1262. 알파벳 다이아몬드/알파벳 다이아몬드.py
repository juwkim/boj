N, R1, C1, R2, C2 = map(int, input().split())
for i in range(R1, R2 + 1):
    for j in range(C1, C2 + 1):
        d = abs(N - 1 - i % (2 * N - 1)) + abs(N - 1 - j % (2 * N - 1))
        print(chr(97 + d % 26) if d < N else '.', end='')
    print()