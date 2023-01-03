from collections import deque

*l, s = input().split()
m, k = map(int, l)
dq = deque(range(m))

for c in s[:-1]:
    if c == 'A':
        dq.rotate(-1)
    else:
        top = dq.popleft()
        dq.rotate(-1)
        dq.appendleft(top)

print(dq[k-1], dq[k], dq[k+1])