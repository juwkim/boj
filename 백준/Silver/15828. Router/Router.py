from collections import deque
dq = deque()
n = int(input())
while (num := int(input())) != -1:
    if num == 0:
        dq.popleft()
    elif len(dq) < n:
        dq.append(num)
if len(dq):
    print(*dq)
else:
    print("empty")