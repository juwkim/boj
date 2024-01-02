import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    V, E = g()
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = g()
        graph[a].append(b)
        graph[b].append(a)
    visited = [0] * (V + 1)
    flag = True
    for i in range(1, V + 1):
        if visited[i]:
            continue
        visited[i] = 1
        stack = [i]
        while stack:
            cur = stack.pop()
            for nxt in graph[cur]:
                if not visited[nxt]:
                    visited[nxt] = -visited[cur]
                    stack.append(nxt)
                elif visited[nxt] == visited[cur]:
                    flag = False
                    break
            if not flag:
                break
        if not flag:
            break
    print("YES" if flag else "NO")