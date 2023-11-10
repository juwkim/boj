import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

C = int(input())
M = int(input())
check = set(g())
for a in check:
    b = C // a
    if a * b == C and b in check:
        print(*sorted([a, b]))
        break