input = __import__('sys').stdin.readline
from collections import defaultdict


def solve(a, b, c):
    
    for name in A[a]:
        if name not in (b, c):
            ans.add((a, name))

    for name in A[b]:
        if name not in (c, a):
            ans.add((b, name))

    for name in A[c]:
        if name not in (a, b):
            ans.add((c, name))
            
    for name in (b, c):
        if name in B[a]:
            ans.add((a, name))

    for name in (c, a):
        if name in B[b]:
            ans.add((b, name))

    for name in (a, b):
        if name in B[c]:
            ans.add((c, name))

A = defaultdict(set)
B = defaultdict(set)

for _ in range(int(input())):
    s, t = input().split()
    A[s].add(t)
    A[t].add(s)

for _ in range(int(input())):
    s, t = input().split()
    B[s].add(t)
    B[t].add(s)

ans = set()
for _ in range(int(input())):
    a, b, c = input().split()
    solve(a, b, c)

print(len(ans) // 2)