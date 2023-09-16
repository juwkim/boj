import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

T = int(input())
a, b, c, d, e = g() + [0] * (5 - T)

ans = (abs(a - c) * [108, 508][a > c] + abs(b - d) * [305, 212][b > d] + e * 707) * 4763
print(ans)