import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, B = g()
gift = []
for _ in range(N):
    P, S = g()
    gift.append((P + S, P // 2 + S))
gift.sort()

ans = 0
for i in range(N):
    cur = gift[i][1]
    if cur > B:
        continue
    cnt = 1
    for j in range(N):
        if i == j:
            continue
        if cur + gift[j][0] <= B:
            cur += gift[j][0]
            cnt += 1
        else:
            break
    ans = max(ans, cnt)
print(ans)