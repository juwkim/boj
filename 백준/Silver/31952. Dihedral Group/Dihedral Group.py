g = lambda: [*map(int, input().split())]

def solve():
    n, m = g()
    if m == 1:
        return 1
    d, t = g(), g()
    i, j = d.index(t[0]), d.index(t[1])
    if min((i - j) % n, (j - i) % n) != 1:
        return 0
    if (j - i) % n == 1:
        return all(d[(i + k) % n] == t[k] for k in range(2, m))
    return all(d[(i - k) % n] == t[k] for k in range(2, m))
print(+solve())