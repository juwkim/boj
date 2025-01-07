import sys
input = sys.stdin.readline
from math import dist

N = int(input())
S = input()
l = [[], []]
for i in range(N): l[S[i] == 'B'].append([*map(int, input().split())])
a, b = l[0], l[1]
print(sum(dist(a[i], a[i + len(a) // 2]) for i in range(len(a) // 2)) + sum(dist(b[i], b[i + len(b) // 2]) for i in range(len(b) // 2)))