import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    C, D1, D2 = map(int, input().split())
    if D1: graph[C].append(D1)
    if D2: graph[C].append(D2)
ans = 0
st = [(1, 1)]
while st:
    cur, cnt = st.pop()
    ans = max(ans, cnt)
    for nxt in graph[cur]:
        st.append((nxt, cnt + 1))
print(ans)