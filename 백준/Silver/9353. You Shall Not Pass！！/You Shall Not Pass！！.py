import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

def dfs(u):
    size[u] = 1
    for v in children[u]:
        dfs(v)
        size[u] += size[v]

for _ in range(int(input())):
    A, B, C = g()
    children = [[] for _ in range(A)]
    parent = [-1] * A
    for __ in range(B):
        F, T = g()
        children[F].append(T)
        parent[T] = F

    size = [0] * A
    for v in range(A):
        if parent[v] == -1:
            dfs(v)

    covered = bytearray(A)
    ans, cnt = 0, 0
    for v in sorted(range(A), key=lambda x: -size[x]):
        if covered[v]:
            continue
        ans += size[v]
        st = [v]
        while st:
            x = st.pop()
            if covered[x]:
                continue
            covered[x] = True
            st.extend(children[x])
        cnt += 1
        if cnt == C:
            break
    print(ans)