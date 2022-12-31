input = __import__('sys').stdin.readline
g = lambda: [*map(int, input().split())]

def Floyd_Warshall(graph, n):
    Set = set()
    for m in range(n):
        for s in range(n):
            for e in range(n):
                if m in (s, e):
                    continue
                dist = graph[s][m] + graph[m][e]
                if dist == graph[s][e]:
                    Set.add((s, e))
                elif dist < graph[s][e]:
                    return -1
    return Set

n = int(input())
graph = [g() for _ in range(n)]
Set = Floyd_Warshall(graph, n)
if Set == -1:
    ans = -1
else:
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (i, j) not in Set:
                ans += graph[i][j]
print(ans)