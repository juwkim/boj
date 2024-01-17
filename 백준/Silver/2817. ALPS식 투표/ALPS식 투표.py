import sys
input = lambda: sys.stdin.readline().rstrip()

from math import lcm

l = 1
for i in range(2, 15):
    l = lcm(l, i)

X = int(input())
buf = []
ans = {}
for _ in range(int(input())):
    name, vote = input().split()
    vote = int(vote)
    if vote * 20 < X:
        continue
    for i in range(1, 15):
        buf.append((vote * l // i, name))
    ans[name] = 0
for _, name in sorted(buf, reverse=True)[:14]:
    ans[name] += 1
for k in sorted(ans.keys()):
    print(k, ans[k])