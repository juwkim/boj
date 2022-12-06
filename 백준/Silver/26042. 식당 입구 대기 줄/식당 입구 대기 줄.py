g = lambda: [*map(int, input().split())]

from collections import deque
dq = deque()
Max, num = 0, 0
for _ in range(int(input())):
    l = g()
    if len(l) == 1:
        dq.popleft()
    else:
        dq.append(l[1])
        if len(dq) > Max or (len(dq) == Max and num > dq[-1]):
            num = dq[-1]
            Max = len(dq)
print(Max, num)