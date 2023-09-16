import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import Counter

N = int(input())
S = input()
P = map(len, S.translate(str.maketrans("HYU", "   ")).split())
D, M = g()
ans = 0
for l in P:
    ans += min(D * l, M + D)
cnt = Counter(S)
HYU = min(cnt['H'], cnt['Y'], cnt['U'])
print(ans if ans else "Nalmeok")
print(HYU if HYU else "I love HanYang University")