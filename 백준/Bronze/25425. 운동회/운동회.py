g = lambda: [*map(int, input().split())]


N, M, a, k = g()

r, q = divmod(a - k, M)
if q:
    r += 1
print(1 + min(N-1, a - k), r + 1)