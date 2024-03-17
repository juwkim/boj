import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N = int(input())
names = [input() for _ in range(N)]
dq = deque(names)
cur = 0
for _ in range(int(input())):
    S, M = map(int, input().split())
    dq.rotate(M % N)
    print(f"{dq[S - 1]} has been eliminated.")
    dq.remove(dq[S - 1])
    N -= 1
if N == 1:
    print(f"{dq[0]} has won.")
else:
    buf = sorted([name for name in dq], key=lambda x: names.index(x))
    print("Players left are", *buf, end='.')