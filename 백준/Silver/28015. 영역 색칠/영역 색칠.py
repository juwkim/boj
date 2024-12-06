import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M = g()
ans = 0
for _ in range(N):
    cnt, cur = 0, 0
    for c in g():
        if c == cur:
            continue
        if c == 0:
            ans += cnt // 2 + 1
            cnt = 0
        else:
            cnt += 1
        cur = c
    if cnt:
        ans += cnt // 2 + 1
print(ans)