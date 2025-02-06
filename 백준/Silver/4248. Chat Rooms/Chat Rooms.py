import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

dq = deque(maxlen=10)
for _ in range(int(input())):
    p = input()
    cnt = 0
    for word in p.split():
        cur = 0
        for c in word:
            if c.isalpha() and c.lower() not in "aeiouy":
                cur += 1
            else:
                cnt = max(cnt, cur)
                cur = 0
        cnt = max(cnt, cur)
        if cnt >= 6:
            break
    if cnt >= 6 or (cnt >= 5 and sum(c >= 5 for s, c in dq) >= 3) or sum(s == p for s, c in dq) >= 2:
        print('n')
    else:
        print('y')
    dq.append((p, cnt))