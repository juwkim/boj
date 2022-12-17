from collections import deque
N, K, P = map(int, input().split())
dq = deque(range(1, K + 1))
ans = []
while dq:
    for _ in range(N - 1):
        dq.popleft()
        dq.rotate(-P)
    ans.append(dq.popleft())
    dq.rotate(-P)
print(*sorted(ans))