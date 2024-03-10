import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
dic = defaultdict(list)
for _ in range(N):
    T, C, *a = input().split()
    dic[tuple(a[:3])].append(C)
for _ in range(M):
    l = dic[tuple(input().split())]
    if len(l) == 0:
        print('!')
    elif len(l) == 1:
        print(l[0])
    else:
        print('?')