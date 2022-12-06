from collections import deque
N = int(input())
dq = deque([N])
for card in range(N - 1, 0, -1):
    dq.appendleft(card)
    dq.rotate(card)
print(*dq)