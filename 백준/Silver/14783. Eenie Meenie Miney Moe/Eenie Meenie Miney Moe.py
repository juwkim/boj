g = lambda: [*map(int, input().split())]

from collections import deque
from itertools import cycle

N, L = g()

dq = deque(range(1, N + 1))
for num in cycle([1 - i for i in g()]):
    dq.rotate(num)
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        break