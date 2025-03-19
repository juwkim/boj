import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

N, Q = map(int, input().split())
dic = defaultdict(list)
for _ in range(N):
    a, b = input().split()
    dic[a[0] + b[0]].append(f"{a} {b}")
for _ in range(Q):
    initial = input()
    match len(dic[initial]):
        case 0: print("nobody")
        case 1: print(dic[initial][0])
        case _: print("ambiguous")