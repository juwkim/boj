from collections import deque

start = 0
for _ in range(4):
    for c in input():
        start = (start << 1) | (c == 'b')

masks = []
for i in range(4):
    for j in range(4):
        m = 0
        for dx, dy in (0, 0), (0, 1), (0, -1), (1, 0), (-1, 0):
            ni, nj = i + dx, j + dy
            if 0 <= ni < 4 and 0 <= nj < 4:
                m |= 1 << (ni * 4 + nj)
        masks.append(m)

dist = [-1] * 65536
dist[start] = 0
dq = deque([start])
ans = "Impossible"
while dq:
    state = dq.popleft()
    if state in (0, 65535):
        ans = dist[state]
        break
    for mask in masks:
        nstate = state ^ mask
        if dist[nstate] == -1:
            dist[nstate] = dist[state] + 1
            dq.append(nstate)
print(ans)