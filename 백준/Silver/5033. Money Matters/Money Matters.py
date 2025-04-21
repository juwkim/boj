import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

n, m = g()
o = [int(input()) for _ in range(n)]
friends = [[] for _ in range(n)]
for _ in range(m):
    x, y = g()
    friends[x].append(y)
    friends[y].append(x)

ans = "POSSIBLE"
visited = bytearray(n)
for i in range(n):
    if visited[i]:
        continue
    res = [i]
    visited[i] = True
    st = [i]
    while st:
        x = st.pop()
        for y in friends[x]:
            if not visited[y]:
                visited[y] = True
                st.append(y)
                res.append(y)
    if sum(o[x] for x in res):
        ans = "IMPOSSIBLE"
        break
print(ans)