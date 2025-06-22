import sys
from collections import deque, defaultdict
input = sys.stdin.readline

while line := input():
    planets = {}
    neighbors = defaultdict(list)
    earth_candidates = []
    for _ in range(int(line)):
        name, val, links = input().split()
        planets[name] = float(val)
        for ch in links:
            if ch == '*':
                earth_candidates.append(name)
            else:
                neighbors[name].append(ch)

    dq = deque(earth_candidates)
    dist = defaultdict(lambda: float('inf'))
    for ec in earth_candidates:
        dist[ec] = 0
    while dq:
        cur = dq.popleft()
        for nb in neighbors[cur]:
            if dist[nb] > dist[cur] + 1:
                dist[nb] = dist[cur] + 1
                dq.append(nb)

    ans = min(planets, key=lambda x: (-planets[x] * .95 ** dist[x]))
    print(f"Import from {ans}")