import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N = int(input())
S = [deque(input().split()) for _ in range(N)]
ans = "Possible"
for l in input().split():
    for i in range(N):
        if S[i] and S[i][0] == l:
            S[i].popleft()
            break
    else:
        ans = "Impossible"
        break
if any(dq for dq in S):
    ans = "Impossible"
print(ans)