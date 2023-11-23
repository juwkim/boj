import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
a1, b1 = g()
a2, b2 = g()

print((min((a1 - a2) % N, (a2 - a1) % N) + min((b1 - b2) % M, (b2 - b1) % M) + 1) // 2)