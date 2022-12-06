g = lambda: [*map(int, input().split())]

from collections import deque
N = int(input())
dq = deque(enumerate(g()))
for _ in range(N):
    idx, num = dq.popleft()
    print(idx + 1, end=' ')
    
    num -= num > 0
    dq.rotate(-num)