input = __import__('sys').stdin.readline
g = lambda: [*map(int, input().split())]

def Floyd_Warshall(graph, n):
    for m in range(1, n + 1):
        for s in range(1, n + 1):
            for e in range(1, n + 1):
                graph[s][e] = min(graph[s][e], graph[s][m] + graph[m][e])

n = int(input())
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]

while (s:= g()) != [-1, -1]:
    a, b = s
    graph[a][b] = 1
    graph[b][a] = 1

Floyd_Warshall(graph, n)

for i in range(1, n + 1):
    graph[i][i] = 0

ans, score = [0], 1e9
for i in range(1, n + 1):
    num = max(graph[i][1:])
    ans.append(num)
    score = min(score, num)

print(score, ans.count(score))
print(*[i for i in range(1, n + 1) if ans[i] == score])