from collections import deque
g = lambda: [*map(int, input().split())]

N, M, K = g()
prefs = [g() for _ in range(N)]

def simulate(retired):
    votes = [0] * (M + 1)
    for county in prefs:
        for cand in county:
            if not (retired >> cand) & 1:
                votes[cand] += 1
                break
    return max(range(1, M + 1), key=lambda x: votes[x])

print(winner:=simulate(0))
dq = deque([(0, 0)])
visited = {0}
while dq:
    retired, cnt = dq.popleft()
    winner = simulate(retired)
    if winner == K:
        print(cnt)
        break
    for i in range(1, M + 1):
        if not (retired >> i) & 1 and i != K:
            new_retired = retired | (1 << i)
            if new_retired not in visited:
                visited.add(new_retired)
                dq.append((new_retired, cnt + 1))