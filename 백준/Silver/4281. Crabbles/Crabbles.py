import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import combinations

N = int(input())
words = {tuple(sorted(input())) for _ in range(N)}
for _ in range(int(input())):
    P = int(input())
    hand = []
    for _ in range(P):
        c, v = input().split()
        hand.append((c, int(v)))
    hand.sort()
    ans = 0
    for k in range(1, P + 1):
        for l in combinations(hand, k):
            C, V = zip(*l)
            if C in words:
                ans = max(ans, sum(V))
    print(ans)