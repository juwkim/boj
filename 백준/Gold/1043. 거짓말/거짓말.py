input = __import__('sys').stdin.readline
g = lambda: [*map(int, input().split())]

from collections import deque
N, M = g()
k, *l = g()
parties = [g()[1:] for _ in range(M)]
visited = bytearray(M)

dq = deque(l)
while dq:
    num = dq.popleft()
    for idx, party in enumerate(parties):
        if visited[idx] == 0:
            if num in party:
                visited[idx] = 1
                for people in party:
                    if people != num:
                        dq.append(people)
print(visited.count(0))