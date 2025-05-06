import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict, deque

graph = defaultdict(list)
method_set = set()
for _ in range(int(input())):
    name, k = input().split()
    method_set.add(name)
    for method in input().split():
        graph[method].append(name)
visited = set()
for method in method_set:
    if method.endswith(":PROGRAM"):
        dq = deque([method])
        visited.add(method)
        while dq:
            u = dq.popleft()
            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    dq.append(v)
print(len(method_set - visited))