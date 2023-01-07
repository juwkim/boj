def g(): return [*map(int, input().split())]

from collections import deque
while sum(l:= g()):
    N, M = l
    dq = deque(range(1, N + 1))
    while len(dq) > 1:
        dq.rotate(1 - M)
        dq.popleft()
    print(dq[0])