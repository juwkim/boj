import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
buf = [[0] * (M + 2) for _ in range(N + 2)]
ans = 0
for i in range(1, N + 1):
    for j in range(1, M + 1):
        l = set(buf[p][q] for p in range(i - 1, i + 2) for q in range(j - 1, j + 2))
        num = 1
        while num in l:
            num += 1
        buf[i][j] = num
        ans = max(ans, num)
print(ans)
for l in buf[1:-1]:
    print(*l[1:-1])