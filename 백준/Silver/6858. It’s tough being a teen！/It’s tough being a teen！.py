import sys
input = sys.stdin.readline
import heapq

in_degree = [0, 1, 0, 0, 2, 1, 0, 1]
graph = [[], [4, 7], [1], [4, 5], [], [], [], []]
while a:=int(input()):
    b = int(input())
    graph[a].append(b)
    in_degree[b] += 1

hq = [i for i in range(1, 8) if in_degree[i] == 0]
heapq.heapify(hq)
ans = []
while hq:
    cur = heapq.heappop(hq)
    ans.append(cur)
    for neighbor in graph[cur]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            heapq.heappush(hq, neighbor)
if len(ans) == 7:
    print(*ans)
else:
    print("Cannot complete these tasks. Going to bed.")