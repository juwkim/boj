import sys
input = sys.stdin.readline
from collections import defaultdict, deque

graph = defaultdict(list)
countries = []
for _ in range(int(input())):
    dest, _, _, _, *origins = input().split()
    countries.append(dest)
    for o in origins:
        graph[o].append(dest)
start = countries[0]
week = {start: 1}
dq = deque([(start, 1)])
while dq:
    cur, w = dq.popleft()
    for nxt in graph[cur]:
        if nxt not in week:
            week[nxt] = w + 1
            dq.append((nxt, w + 1))
for country in sorted(countries):
    print(week.get(country, 0))