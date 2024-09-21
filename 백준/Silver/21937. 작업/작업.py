import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

N, M = g()
d = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = g()
    d[B].append(A)
ans = 0
st = [X:=int(input())]
visited = bytearray(N + 1)
visited[X] = 1
while st:
    x = st.pop()
    for y in d[x]:
        if not visited[y]:
            visited[y] = 1
            ans += 1
            st.append(y)
print(ans)