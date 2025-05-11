from collections import deque
g = lambda: [*map(int, input().split())]

N, M, K = g()
prefs = [g() for _ in range(N)]

def simulate(active):
    votes = [0] * (M + 1)
    for county in prefs:
        for cand in county:
            if active[cand]:
                votes[cand] += 1
                break
    return max(range(1, M + 1), key=lambda x: votes[x])

active = tuple([1] * (M + 1))
print(winner:=simulate(active))
dq = deque([(active, 0)])
visited = {active}
while dq:
    active, cnt = dq.popleft()
    winner = simulate(active)
    if winner == K:
        print(cnt)
        break
    for i in range(1, M + 1):
        if active[i] and i != K:
            new_active = list(active)
            new_active[i] = 0
            new_active = tuple(new_active)
            if new_active not in visited:
                visited.add(new_active)
                dq.append((new_active, cnt + 1))