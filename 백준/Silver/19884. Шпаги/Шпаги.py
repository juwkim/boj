import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import deque

n, k = g()
l, *a = sorted(enumerate(g()), key=lambda x: x[1], reverse=True)
ans = [0] * n
dq = deque([l, l])
for i, new in a:
    idx, ori = dq.popleft()
    if ori - new >= k:
        ans[i] = idx + 1
        dq.append((i, new))
        dq.append((i, new))
    else:
        print(-1)
        break
else:
    print(*ans)