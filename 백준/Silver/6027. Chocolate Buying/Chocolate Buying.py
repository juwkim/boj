import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, B = g()
ans = 0
for P, C in sorted(g() for _ in range(N)):
    if B < P * C:
        ans += B // P
        break
    ans += C
    B -= P * C
print(ans)