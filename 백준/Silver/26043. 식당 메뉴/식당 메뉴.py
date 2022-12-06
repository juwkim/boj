from collections import deque
dq = deque()
A, B = [], []
for _ in range(int(input())):
    num, *l = map(int, input().split())
    if num == 1:
        dq.append(l)
    else:
        a, b = dq.popleft()
        if l[0] == b: A.append(a)
        else: B.append(a)
A.sort()
B.sort()
C = sorted([a for a, b in dq])
if A: print(*A)
else: print('None')
if B: print(*B)
else: print('None')
if C: print(*C)
else: print('None')