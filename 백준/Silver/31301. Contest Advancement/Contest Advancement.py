import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n, k, c = g()
cnt = [0] * (n + 1)
ans, buf = [], []
for i in range(n):
    t, s = g()
    cnt[s] += 1
    if cnt[s] <= c:
        ans.append((i, t))
        if len(ans) == k:
            break
    else:
        buf.append((i, t))
if len(ans) < k:
    ans.extend(buf[:k - len(ans)])
ans.sort()
print(*[team[1] for team in ans])