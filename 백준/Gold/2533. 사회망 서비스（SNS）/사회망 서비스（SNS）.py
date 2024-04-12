import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**6 + 1)

N = int(input())
mem = [-1] * (N + 1)
graph = defaultdict(list)
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def solve(i, parent=-1):
    if mem[i] != -1:
        return mem[i]
    a = 1
    for j in graph[i]:
        if j == parent:
            continue
        a += solve(j, i)

    b = 0
    for j in graph[i]:
        if j == parent:
            continue
        b += 1
        for k in graph[j]:
            if k == i:
                continue
            b += solve(k, j)
    mem[i] = min(a, b)
    return mem[i]
print(solve(1, 0))