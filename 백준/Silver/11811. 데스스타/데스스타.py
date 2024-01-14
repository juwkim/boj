import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
m = [g() for _ in range(N)]
a = [0] * N
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        a[i] |= m[i][j]
        a[j] |= m[i][j]
print(*a)