from collections import deque
N, M = map(int, input().split())
Map = tuple(input() for _ in range(N))
visited_smooth = tuple(bytearray(M) for _ in range(N))
visited_break = tuple(bytearray(M) for _ in range(N))

ans = -1
dq = deque([(1, 0, 0, 0)])
while dq:
    cnt, used, x, y = dq.popleft()
    for a, b in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
        if 0 <= a < N and 0 <= b < M:
            if a == N - 1 and b == M - 1:
                ans = cnt + 1
                break
            if used and visited_break[a][b] == 0 and Map[a][b] == '0':
                visited_break[a][b] = 1
                dq.append((cnt + 1, used, a, b))
            elif not used and visited_smooth[a][b] == 0:
                visited_smooth[a][b] = 1
                dq.append((cnt + 1, Map[a][b] == '1', a, b))
    else:
        continue
    break
if N == 1 and M == 1:
    ans = 1
print(ans)