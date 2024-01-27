import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
parent = [0, *[int(input()) for _ in range(n)]]
h = [0 for _ in range(n + 1)]
def dist(i):
    if parent[i] == -1:
        return 0
    if h[i]:
        return h[i]
    h[i] = dist(parent[i]) + 1
    return h[i]
for i in range(1, n + 1):
    h[i] = dist(i)
print(*h[1:])