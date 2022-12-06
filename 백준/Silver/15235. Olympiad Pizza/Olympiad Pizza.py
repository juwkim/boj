g = lambda: [*map(int, input().split())]

from collections import deque
N = int(input())
ans = [0] * N
dq = deque()
dq.extend([[idx, num] for idx, num in enumerate(g())])
cnt = 1
while dq:
    tmp = dq[0]
    tmp[1] -= 1
    if tmp[1]:
        dq.rotate(-1)
    else:
        ans[tmp[0]] = cnt
        dq.popleft()
    cnt += 1
print(*ans)