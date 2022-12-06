g = lambda: [*map(int, input().split())]

from collections import deque
N = int(input())
nums = g()
dq = deque(range(N))
start = 1 - nums[0]
while len(dq) > 1:
    dq.rotate(start)
    dq.popleft()
    start = 1 - nums[dq[0]]
print(dq[0] + 1)