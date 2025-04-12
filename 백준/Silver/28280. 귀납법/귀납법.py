import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    k = int(input())
    dq = deque([(k, 0)])
    visited = {k}
    while dq:
        n, cnt = dq.popleft()
        if n == 1:
            print(cnt)
            break
        if n + 1 not in visited:
            visited.add(n + 1)
            dq.append((n + 1, cnt + 1))
        if n % 2 == 0 and n // 2 not in visited:
            visited.add(n // 2)
            dq.append((n // 2, cnt + 1))