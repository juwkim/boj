import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()

cntA, last = 0, -100
for A in sorted(g()):
    if A >= last + 100:
        cntA += 1
        last = A

cntB, last = 0, -360
for B in sorted(g()):
    if B >= last + 360:
        cntB += 1
        last = B

print(cntA, cntB)