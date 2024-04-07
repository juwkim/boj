import sys
input = sys.stdin.readline
from itertools import product

def solve(i):
    s.add(i)
    for j in network[i]:
        solve(j)
N = int(input())
network = [[] for _ in range(N - 1)]
for i in range(N - 1):
    num = int(input())
    if num != N:
        network[num - 1].append(i)

buf = set()
for l in product((0, 1), repeat=N-1):
    s = set()
    for i in range(N - 1):
        if l[i]:
            solve(i)
    buf.add(tuple(sorted(s)))
print(len(buf))