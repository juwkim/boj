from collections import deque

target = tuple(map(int, input().split()))
cur = (1, 2, 3, 4, 5, 6, 7, 8)
dq = deque([(cur, 0)])
visited = {cur}
while dq:
    state, cnt = dq.popleft()
    if state == target:
        print(cnt)
        break
    for l in (7, 6, 5, 4, 3, 2, 1, 0), (3, 0, 1, 2, 5, 6, 7, 4), (0, 2, 5, 3, 4, 6, 1, 7), (4, 1, 2, 3, 0, 5, 6, 7):
        new = tuple(state[c] for i, c in enumerate(l))
        if new not in visited:
            visited.add(new)
            dq.append((new, cnt + 1))