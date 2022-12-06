import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

N = int(input())
graph = [[] for _ in range(1 + N)]
for _ in range(int(input())):
    A, B = g()
    graph[A].append(B)
    graph[B].append(A)

ans = set()
for num in graph[1]:
    ans.update(graph[num])
ans.update(graph[1])
print(len(ans) - (1 in ans))