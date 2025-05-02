def solve():
    n, k, *a = map(int, open(0).read().split())
    for p in range(1, n // k + 1):
        for start in range(n - p * k + 1):
            pattern = a[start:start + p]
            if all(a[start + i * p: start + (i + 1) * p] == pattern for i in range(1, k)):
                print(p)
                print(*pattern)
                return
    print(-1)
solve()