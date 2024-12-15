import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from collections import deque

N, H, L = g()
x = g()
HI = [1e9] * N
for num in x: HI[num] = 0
mat = [[] for _ in range(N)]
for _ in range(L):
    a, b = g()
    mat[a].append(b)
    mat[b].append(a)
dq = deque(x)
while dq:
    u = dq.popleft()
    for v in mat[u]:
        if HI[v] > HI[u] + 1:
            HI[v] = HI[u] + 1
            dq.append(v)
print(max(range(N), key=lambda i: HI[i]))