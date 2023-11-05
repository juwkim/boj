import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import defaultdict

dic = defaultdict(int)
N, L = g()
for _ in range(N):
    dic[len(input().replace('0', ' ').split())] += 1

k = max(dic)
v = dic[k]
print(k, v)