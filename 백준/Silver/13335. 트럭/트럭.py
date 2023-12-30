import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import deque

n, w, L = g()
dq = deque()
time, weight = 0, 0
for wei in g():
    while weight + wei > L:
        top_wei, top_time = dq.popleft()
        weight -= top_wei
        time = max(time, top_time + w)
    dq.append((wei, time))
    weight += wei
    time += 1
time += w
print(time)