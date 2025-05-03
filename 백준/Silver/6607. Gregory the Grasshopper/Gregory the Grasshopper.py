from collections import deque

for l in open(0):
    R, C, GR, GC, LR, LC = map(int, l.split())
    visited = [bytearray(C + 1) for _ in range(R + 1)]
    visited[GR][GC] = True
    dq = deque([(GR, GC, 0)])
    ans = "impossible"
    while dq:
        r, c, dist = dq.popleft()
        if (r, c) == (LR, LC):
            ans = dist
            break
        for dr, dc in (-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1):
            nr, nc = r + dr, c + dc
            if 0 < nr <= R and 0 < nc <= C and not visited[nr][nc]:
                visited[nr][nc] = True
                dq.append((nr, nc, dist + 1))
    print(ans)