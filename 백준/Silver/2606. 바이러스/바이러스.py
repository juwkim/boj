import sys
input = lambda: sys.stdin.readline().rstrip()

g = lambda: [*map(int, input().split())]
N = int(input())
graph = {i: [] for i in range(1, 1 + N)}
for _ in range(int(input())):
    a, b = g()
    graph[a].append(b)
    graph[b].append(a)
ans = 0
check = [0 for _ in range(N+1)]
check[1] = 1
def dfs(num):
    while graph[num]:
        tmp = graph[num].pop()
        if not check[tmp]:
            check[tmp] = 1
            dfs(tmp)
dfs(1)
print(sum(check) - 1)