from collections import deque
g = lambda: [*map(int, input().split())]

N, M, K = g()
prefs = [g() for _ in range(N)]

def simulate(retired):
    votes = [0] * (M + 1)
    for county in prefs:
        for cand in county:
            if not retired & 1 << cand - 1:
                votes[cand] += 1
                break
    return max(range(1, M + 1), key=lambda x: votes[x])

print(simulate(0))
dq = deque([(0, 0)])
visited = [0] * (1 << M)
while dq:
    retired, cnt = dq.popleft()
    if simulate(retired) == K:
        print(cnt)
        break
    for i in range(M):
        if i + 1 != K and not retired & 1 << i:
            new_retired = retired | 1 << i
            if not visited[new_retired]:
                visited[new_retired] = 1
                dq.append((new_retired, cnt + 1))