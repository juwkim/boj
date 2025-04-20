import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

for _ in range(int(input())):
    n, m, l = map(int, input().split())
    domino = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        domino[x].append(y)
    fallen = bytearray(n + 1)
    for _ in range(l):
        z = int(input())
        if not fallen[z]:
            st = [z]
            fallen[z] = True
            while st:
                for v in domino[st.pop()]:
                    if not fallen[v]:
                        fallen[v] = True
                        st.append(v)
    print(sum(fallen))