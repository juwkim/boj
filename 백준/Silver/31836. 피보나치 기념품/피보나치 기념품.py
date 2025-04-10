N = int(input())
q = N // 3
if N % 3 == 2:
    print(q + 1)
    print(*range(2, N + 1, 3))
    print(2 * q + 1)
    print(*range(1, N, 3), *range(3, N - 1, 3))
else:
    print(q)
    print(*range(3, N + 1, 3))
    print(2 * q)
    print(*range(1, N, 3), *range(2, N, 3))