N, D = map(int, input().split())
if N&1:
    print(*range(D - N // 2, D + N // 2 + 1))
else:
    print(*range(D - N // 2, D), *range(D + 1, D + N // 2 + 1))