import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
from itertools import combinations

N = int(input())
A = [0] + g()
graph = [[]] + [{*g()[1:]} for _ in range(N)]
ans = float('inf')
for i in range(1, N // 2 + 1):
    for comb in map(set, combinations(range(1, N + 1), i)):
        def dfs(l):
            sum = 0
            x, *nodes = l
            nodes = {*nodes} - {x}
            st = [x]
            visited = bytearray(N + 1)
            visited[x] = 1
            while st:
                u = st.pop()
                sum += A[u]
                for v in graph[u]:
                    if v in nodes and not visited[v]:
                        visited[v] = 1
                        nodes.remove(v)
                        st.append(v)
            if nodes:
                return 0
            return sum
        a = dfs(comb)
        if a:
            b = dfs({*range(1, N + 1)} - comb)
            if b:
                ans = min(ans, abs(a - b))
print(ans if ans != float('inf') else -1)