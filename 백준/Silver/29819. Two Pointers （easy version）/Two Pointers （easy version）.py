import sys
g = lambda: map(int, sys.stdin.readline().split())

for _ in range(int(input())):
    n, *l = g()
    A, B = sorted(l)
    cities = sorted(g())
    ans = 1e18
    for i in range(n + 1):
        dist = 0
        if i:
            a_min, a_max = cities[0], cities[i - 1]
            dist += min(abs(A - a_min), abs(A - a_max)) + a_max - a_min
        if i < n:
            b_min, b_max = cities[i], cities[-1]
            dist += min(abs(B - b_min), abs(B - b_max)) + b_max - b_min
        ans = min(ans, dist)
    print(ans)