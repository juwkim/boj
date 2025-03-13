N = int(input())
graph = [[] for _ in range(N)]
for i in range(N):
    j = (3 * i + 7) % N
    graph[i].append(j)
    graph[j].append(i)
    
visited = bytearray(N)
st = [0]
visited[0] = 1
while st:
    i = st.pop()
    for j in graph[i]:
        if not visited[j]:
            visited[j] = 1
            st.append(j)
if all(visited):
    print('YES')
else:
    print('NO')
    i = 1
    while visited[i]:
        i += 1
    print(0, i)