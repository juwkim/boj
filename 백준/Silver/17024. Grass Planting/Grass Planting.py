import sys
input = sys.stdin.readline

N = int(input())
graph = [0] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a] += 1
    graph[b] += 1
print(max(graph) + 1)