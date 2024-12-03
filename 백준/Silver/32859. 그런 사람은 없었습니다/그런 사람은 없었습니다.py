import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

N, M = g()
S = int(input())
ans, d, cnt = [], {}, 0
for _ in range(M):
    i, t = g()
    if t:
        if i in d and d[i][0] == 0:
            del d[i]
        else:
            d[i] = (1, cnt)
    else:
        cnt += 1
        if i not in d:
            d[i] = (0, cnt)
            continue
        if cnt - d[i][1] > S:
            ans.append(i)
        del d[i]
for k, (t, c) in d.items():
    if t and cnt - c >= S:
        ans.append(k)          
if ans:
    print(*sorted(ans))
else:
    print(-1)