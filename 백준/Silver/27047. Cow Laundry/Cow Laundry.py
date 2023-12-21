import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
buf = [g() for _ in range(N)]
a = [0] * N
for i in range(N):
    for j in range(N):
        if buf[i][1] == buf[j][0]:
            a[j] = i
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        ans += a[i] > a[j]
print(ans)