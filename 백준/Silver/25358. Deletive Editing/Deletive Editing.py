import sys
input = sys.stdin.readline
from collections import defaultdict

for _ in range(int(input())):
    s, t = input().split()
    dic = defaultdict(list)
    for i in range(len(s)): dic[s[i]].append(i)
    ans = "YES"
    prv = len(s)
    for i in range(len(t) - 1, -1, -1):
        l = dic[t[i]]
        if not l or l[-1] > prv:
            ans = "NO"
            break
        prv = l.pop()
    print(ans)