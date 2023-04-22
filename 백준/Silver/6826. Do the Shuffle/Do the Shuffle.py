from collections import deque

dq = deque('ABCDE')
while (b := int(input())) != 4:
    n = int(input())
    if b == 1:
        dq.rotate(-n)
    elif b == 2:
        dq.rotate(n)
    elif n & 1:
        dq[0], dq[1] = dq[1], dq[0]
print(*dq)