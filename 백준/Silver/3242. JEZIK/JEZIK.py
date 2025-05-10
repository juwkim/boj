*lines, _ = open(0)
n = len(lines)
graph = [[] for _ in range(n + 1)]
for i, line in enumerate(lines):
    instr = line.split()
    if instr[0] == "RADI":
        graph[i].append(i + 1)
    else:
        graph[i].append(int(instr[1]) - 1)
        if len(instr) == 4:
            graph[i].append(int(instr[3]) - 1)
visited = bytearray(n + 1)
visited[0] = True
visited[n] = True
st = [0]
while st:
    u = st.pop()
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            st.append(v)
print(visited.count(False))