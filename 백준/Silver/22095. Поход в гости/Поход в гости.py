import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

from collections import deque
for _ in range(int(input())):
    n, m = g()
    buf = [deque() for _ in range(n + 1)]
    for _ in range(m):
        a, b = g()
        if buf[a]:
            present = buf[a].popleft()
            buf[b].append(present)
            print(['NO', 'YES'][present == b])
        else:
            buf[b].append(a)
            print('NO')