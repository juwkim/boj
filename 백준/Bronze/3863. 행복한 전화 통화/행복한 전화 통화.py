import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
while (s:= input().rstrip()) != '0 0':
    buf = []
    N, M = map(int, s.split())
    for _ in range(N):
        a, b, s, d = g()
        buf.append((s, s + d))
    for _ in range(M):
        s, d = g()
        print(sum(s == x or (s < x and s + d > x) or (s > x and s < y) for x, y in buf))