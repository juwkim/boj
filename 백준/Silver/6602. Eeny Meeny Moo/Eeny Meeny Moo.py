import sys
input = sys.stdin.readline
from collections import deque
ans = [0, 0, 0]
for n in range(3, 150):
    m = 1
    while True:
        dq = deque(range(n))
        for _ in range(n - 1):
            dq.popleft()
            dq.rotate(-m)
        if dq[0] == 1:
            ans.append(m + 1)
            break
        m += 1
while n:=int(input()):
    print(ans[n])