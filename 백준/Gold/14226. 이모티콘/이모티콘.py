from collections import deque

ans = 0
S = int(input())
dq = deque([(1, 0, 0)])
visited = {(1, 0, 0)}
while dq:
    cur, clip, cnt = dq.popleft()
    if cur == S:
        print(cnt)
        break
    if (cur, cur, cnt + 1) not in visited:
        visited.add((cur, cur, cnt + 1))
        dq.append((cur, cur, cnt + 1))
    if (cur + clip, clip, cnt + 1) not in visited:
        visited.add((cur + clip, clip, cnt + 1))
        dq.append((cur + clip, clip, cnt + 1))
    if cur - 1 >= 0 and (cur - 1, clip, cnt + 1) not in visited:
        visited.add((cur - 1, clip, cnt + 1))
        dq.append((cur - 1, clip, cnt + 1))