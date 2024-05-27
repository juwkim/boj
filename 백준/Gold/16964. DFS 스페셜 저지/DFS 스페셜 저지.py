import sys
input = sys.stdin.readline

N = int(input())
graph = [set() for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

path = [*map(int, input().split())]
if path[0] != 1:
    print(0)
    exit(0)

i = 0
visited = bytearray(N + 1)
def solve():
    global i
    if i == N - 1:
        print(1)
        exit()
    v = path[i]
    i += 1
    visited[v] = 1
    for _ in range(len(graph[v])):
        if path[i] in graph[v] and not visited[path[i]]:
            solve()
solve()
print(0)