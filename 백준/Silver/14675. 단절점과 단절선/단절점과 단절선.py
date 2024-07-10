import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for _ in range(int(input())):
    t, k = map(int, input().split())
    if t == 1:
        print('yes' if len(graph[k]) >= 2 else 'no')
    else:
        print('yes')