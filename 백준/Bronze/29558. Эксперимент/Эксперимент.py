N, D = map(int, input().split())
P = N//2
if N&1:
    print(*range(D - P, D + P + 1))
else:
    print(*range(D - P, D), *range(D + 1, D + P + 1))