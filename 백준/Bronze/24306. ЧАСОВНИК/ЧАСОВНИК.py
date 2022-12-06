g = lambda: [*map(int, input().split())]

a, b, c = g()

def solve(t):
    t %= a * b * c
    h = t / (a * b * c)
    t %= b * c
    m = t / (b * c)
    t %= c
    s = t / c
    return h, m, s

for t in range(a * b * c):
    h1, m1, s1 = solve(t)
    h2, m2, s2 = solve(t+1)
    if h1 > m1 > s1 and h2 <= m2 <= s2:
        print((a * b * c - 1) // (t + 1))
        break