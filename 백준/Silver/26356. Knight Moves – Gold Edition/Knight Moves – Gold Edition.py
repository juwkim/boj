import sys
from collections import deque
input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    N, R1, C1, R2, C2 = map(int, input().split())
    visited = [bytearray(N + 1) for _ in range(N + 1)]
    visited[R1][C1] = True
    dq = deque([(R1, C1, 0)])
    while dq:
        r, c, dist = dq.popleft()
        if r == R2 and c == C2:
            print(f"Case #{tc}: {dist}\n")
            break
        for dr, dc in (-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1):
            nr, nc = r + dr, c + dc
            if 0 < nr <= N and 0 < nc <= N and not visited[nr][nc]:
                visited[nr][nc] = True
                dq.append((nr, nc, dist + 1))