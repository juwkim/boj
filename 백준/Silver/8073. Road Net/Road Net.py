def g(): return [*map(int, input().split())]

N = int(input())
graph = [g() for _ in range(N)]
for s in range(N - 1):
    for e in range(s + 1, N):
        if all(graph[s][m] + graph[m][e] > graph[s][e] for m in range(N) if m not in (s, e)):
            print(s + 1, e + 1)