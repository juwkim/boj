import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque, defaultdict

dq = deque()
dic = defaultdict(int)
cost = 0
for _ in range(int(input())):
    s = input()
    if s[0] == '+':
        k = int(s.split()[1])
        dq.append(k)
        dic[k] += 1
        cost += k
    elif s == '-':
        k = dq.popleft()
        dic[k] -= 1
        cost -= k
    else:
        q, r = divmod(cost, len(dq))
        if r:
            print(0)
        else:
            print(dic[q])