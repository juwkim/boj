import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, X, Y = g()
M, B = map(sorted, zip(*[g() for _ in range(N)]))
ans = 0
for m, b in zip(M, B):
    if m > b:
        ans += (m - b) * Y
    else:
        ans += (b - m) * X
print(ans)