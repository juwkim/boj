import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
t = [1] * (N + 1)
for _ in range(M):
    k, s, e = g()
    if s >= t[k]:
        t[k] = e
        print("YES")
    else:
        print("NO")