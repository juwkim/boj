import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import defaultdict

dic = {}
for _ in range(int(input())):
    P, S = input().split()
    P = int(P)
    for idx, c in enumerate(S):
        if c in dic:
            if type(dic[c]) == int:
                P0 = dic[c]
                dic[c] = [-(P - P0), P0, idx]
        else:
            dic[c] = P

ans = min(dic, key=lambda x: dic[x])
print(ans)