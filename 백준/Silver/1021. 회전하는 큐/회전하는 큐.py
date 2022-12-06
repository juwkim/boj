g = lambda: [*map(int, input().split())]

from collections import deque
N, M = g()
dq = deque(range(1, 1 + N))
ans = 0
for num in g():
    idx = dq.index(num)
    tmp = len(dq) - idx
    if tmp < idx:
        ans += tmp
        dq.rotate(tmp)
    else:
        ans += idx
        dq.rotate(-idx)
    dq.popleft()
print(ans)