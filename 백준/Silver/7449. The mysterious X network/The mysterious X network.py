import sys
input = sys.stdin.readline
from collections import deque

while True:
    try:
        n = int(input())
    except:
        break
    graph = [[] for _ in range(n)]
    for _ in range(n):
        c1, nc, *nums = map(int, input().split())
        graph[c1] = nums
    c1, c2 = map(int, input().split())
    dq = deque([(c1, -1)])
    visited = bytearray(n)
    visited[c1] = 1
    while dq:
        node, dist = dq.popleft()
        if node == c2:
            print(c1, c2, dist)
            break
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                dq.append((neighbor, dist + 1))
    print()