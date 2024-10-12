from collections import deque

S = int(input())
dq = deque([(1, 0, 0)])
visited = {(1, 0, 0)}
while dq:
    cur, clip, cnt = dq.popleft()
    if cur == S:
        print(cnt)
        break
    for l in (cur, cur, cnt + 1), (cur + clip, clip, cnt + 1), (cur - 1, clip, cnt + 1):
        if l not in visited and l[0]:
            visited.add(l)
            dq.append(l)