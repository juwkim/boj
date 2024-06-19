import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())
from collections import Counter

N, K = g()
t = Counter(g())
ans = sum(v // K for v in t.values())
for _ in range(int(input())):
    a, b = g()
    ans += (t[a] - b) // K - t[a] // K
    t[a] -= b
    print(ans)