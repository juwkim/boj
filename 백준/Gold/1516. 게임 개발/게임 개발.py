import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
time = [0] * (N + 1)
prev = [[] for _ in range(N + 1)]
next = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    t, *p, _ = map(int, input().split())
    prev[i] = set(p)
    time[i] = t
    for num in p:
        next[num].append(i)
ans = [0] * (N + 1)
dq = deque([i for i in range(1, N + 1) if not prev[i]])
while dq:
    cur = dq.popleft()
    ans[cur] += time[cur]
    for num in next[cur]:
        ans[num] = max(ans[num], ans[cur])
        prev[num].remove(cur)
        if not prev[num]:
            dq.append(num)
print(*ans[1:], sep='\n')