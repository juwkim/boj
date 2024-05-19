import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque, defaultdict

dic = defaultdict(list)
died = set()
new = True
l = []
for _ in range(int(input())):
    s = input()
    if s[0] == '+':
        _, father, son = s.split()
        dic[father].append(son)
        new = True
    elif s[0] == '-':
        _, name = s.split()
        died.add(name)
        new = True
    else:
        d = int(s.split()[1]) - 1
        if new:
            l = []
            dq = deque(['M'])
            while dq:
                cur = dq.popleft()
                if cur not in died:
                    l.append(cur)
                for son in dic[cur]:
                    dq.append(son)
        print(l[d] if d < len(l) else '-')
        new = False