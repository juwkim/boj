import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K = g()
buf = []
for num in g():
    P = num * 100 // N
    for g, cut in enumerate((4, 11, 23, 40, 60, 77, 89, 96, 100), 1):
        if P <= cut:
            buf.append(g)
            break
print(*buf)