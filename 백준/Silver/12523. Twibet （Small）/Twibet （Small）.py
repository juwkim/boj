import sys
input = sys.stdin.readline
from collections import deque

for tc in range(1, 1 + int(input())):
    N = int(input())
    nums = [[] for _ in range(N + 1)]
    for i, F in enumerate(map(int, input().split()), 1):
        nums[F].append(i)
    print(f"Case #{tc}:")
    for i in range(1, N + 1):
        dq = deque([i])
        visited = bytearray(N + 1)
        visited[i] = 1
        cnt = 1
        while dq:
            cur = dq.popleft()
            for nxt in nums[cur]:
                if visited[nxt]:
                    continue
                dq.append(nxt)
                visited[nxt] = 1
                cnt += 1
        print(cnt)