g = lambda: [*map(int, input().split())]

from collections import deque

N, K = g()
dq = deque(range(1, N+1))
ans = []
while dq:
    dq.rotate(1 - K)
    ans.append(dq.popleft())
print('<' + ', '.join(map(str, ans)) + '>')