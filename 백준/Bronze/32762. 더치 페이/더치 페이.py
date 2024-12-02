import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, M = g()
for _ in range(N): input()
print(sum(g()[1] for _ in range(M)) / N)