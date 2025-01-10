import sys
input = sys.stdin.readline
from collections import deque

while n:=int(input()):
    dq = deque()
    for _ in range(n):
        c1, c2 = map(int, input().split())
        if c1 != c2:
            dq.append([c1, c2])
    ans = 0
    while len(dq) >= 2:
        ans += 1
        num = min(dq[0])
        dq[0].remove(num)
        if num in dq[1]:
            dq[1].remove(num)
        else:
            dq[1].append(num)
        if not dq[0]:
            dq.popleft()
        else:
            dq.rotate(-1)
        if not dq[0]:
            dq.popleft()
    print(ans)