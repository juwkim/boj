from collections import deque

N, K = map(int, input().split())
dq = deque(range(1, N + 1))
while len(dq) > 1:
    dq.rotate(-1)
    for _ in range(min(K, len(dq)) - 1):
        dq.popleft()
print(dq[0])