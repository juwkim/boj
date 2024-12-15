import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, M = g()
C = [[0] * (N + 1)] + [[0] + g() for _ in range(N)]
visited = bytearray(N + 1)
visited[M] = 1
st = [M]
print(M)
while st:
    nst = []
    while st:
        x = st.pop()
        for i in range(1, N + 1):
            if x != i and not visited[i] and C[x][i]:
                visited[i] = 1
                nst.append(i)
    st = sorted(nst)
    print(*st)