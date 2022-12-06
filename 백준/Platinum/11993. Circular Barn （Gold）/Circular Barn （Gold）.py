from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip('\n')

N = int(input())
r = [[i] * int(input()) for i in range(N)]
dq = deque()
while True:
    for idx in range(N):
        if len(dq):
            dq.extend(r[idx])
            r[idx] = [dq.popleft()]
        elif len(r[idx]) > 1:
            dq.extend(r[idx][:-1])
            r[idx] = [r[idx][0]]
    if len(dq) == 0 and all(len(line) == 1 for line in r):
        break
ans = sum(((i - r[i][0]) % N) ** 2 for i in range(N))
print(ans)