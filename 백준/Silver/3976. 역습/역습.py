import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

for _ in range(int(input())):
    _, a, b, s1, s2 = g()
    for p1, d1, p2, d2 in zip(g(), g(), g(), g()):
        a, b = min(a + d1, b + p2), min(b + d2, a + p1)
    print(min(a + s1, b + s2))