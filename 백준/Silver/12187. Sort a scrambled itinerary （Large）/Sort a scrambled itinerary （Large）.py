import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque
for tc in range(1, 1 + int(input())):
    N = int(input())
    s, e = [], []
    for _ in range(N):
        s.append(input())
        e.append(input())
    dq = deque([0])
    visited = bytearray(N)
    visited[0] = 1
    for _ in range(N - 1):
        for i in range(N):
            if s[dq[0]] == e[i]:
                visited[i] = 1
                dq.appendleft(i)
                break
            if e[dq[-1]] == s[i]:
                visited[i] = 1
                dq.append(i)
                break
    ans = []
    for i in dq:
        ans.append(f"{s[i]}-{e[i]}")
    print(f"Case #{tc}:", *ans)