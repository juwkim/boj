import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

N, M = g()
ans, p = [], 0
for K, Z in [g() for _ in range(M)][::-1]:
    ans.append(cur:=min(Z, N + 1 - K - p))
    p += cur
print(N - p)
print(*ans[::-1], sep='\n')