from collections import deque

def solve(x):
    cnt = [-1] * (1 << N)
    cnt[1 << N - 1] = 0
    dq = deque([1 << N - 1])
    while dq:
        i = dq.popleft()
        if i == x:
            return cnt[i]
        for p in (0, 1 << N):
            ni = i + p >> 1
            if cnt[ni] == -1:
                cnt[ni] = cnt[i] + 1
                dq.append(ni)

N, x, y = map(int, input().split())
print(max(solve(x), solve(y)))