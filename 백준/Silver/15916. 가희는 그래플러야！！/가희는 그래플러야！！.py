def solve():
    n, *y, k = map(int, open(0).read().split())
    if y[0] == k:
        return 'T'
    for i in range(1, n):
        if (y[i - 1] - i * k) * (y[i] - (i + 1) * k) <= 0:
            return 'T'
    return 'F'
print(solve())