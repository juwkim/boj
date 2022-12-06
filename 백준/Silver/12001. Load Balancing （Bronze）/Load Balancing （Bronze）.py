import sys
input = lambda: sys.stdin.readline().rstrip('\n')
g = lambda: [*map(int, input().split())]

N, B = g()
cows = [g() for _ in range(N)]

ans = N
res = set()
for i in range(N):
    for j in range(N):
        x = cows[i][0]
        y = cows[j][1]
        if (x, y) not in res:
            res.add((x, y))
        cnt = [0, 0, 0, 0]
        for k in range(N):
            s, t = cows[k]
            cnt[(s > x) + (t > y) * 2] += 1
        ans = min(ans, max(cnt))
print(ans)
    