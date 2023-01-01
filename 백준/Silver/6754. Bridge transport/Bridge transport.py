from collections import deque
W, N = int(input()), int(input())
ans, cur, dq = N, 0, deque()
for i in range(N):
    if len(dq) >= 4:
        cur -= dq.popleft()
    num = int(input())
    cur += num
    dq.append(num)
    if cur > W:
        ans = i
        break
print(ans)