import sys
input = sys.stdin.readline

n = int(input())
deg = [-2] * (n + 1)
for _ in range(n - 1):
    u, v = map(int, input().split())
    deg[u] += 1
    deg[v] += 1
print(sum(max(0, d) for d in deg))