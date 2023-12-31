import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

C, R = g()
N = int(input())
def f():
    d, off = g()
    r, c = -1, -1
    match d:
        case 1:
            r, c = 0, off
        case 2:
            r, c = R, off
        case 3:
            r, c = off, 0
        case 4:
            r, c = off, C
    return r, c
pos = [f() for _ in range(N)]
r1, c1 = f()
ans = 0
for r2, c2 in pos:
    if abs(r1 - r2) == R:
        ans += R + min(c1 + c2, 2 * C - c1 - c2)
    elif abs(c1 - c2) == C:
        ans += C + min(r1 + r2, 2 * R - r1 - r2)
    else:
        ans += abs(r1 - r2) + abs(c1 - c2)
print(ans)