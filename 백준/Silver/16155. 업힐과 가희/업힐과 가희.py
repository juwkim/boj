import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
from math import gcd

N = int(input())
X, H = zip(*[g() for _ in range(N + 1)])
S, E = g()
for i in range(N):
    if X[i] <= S <= X[i + 1]:
        a1, b1 = H[i] * (X[i + 1] - X[i]) + (H[i + 1] - H[i]) * (S - X[i]), (X[i + 1] - X[i])
    if X[i] <= E <= X[i + 1]:
        a2, b2 = H[i] * (X[i + 1] - X[i]) + (H[i + 1] - H[i]) * (E - X[i]), (X[i + 1] - X[i])
s, t = abs(a1 * b2 - a2 * b1), b1 * b2 * (E - S)
if s % t:
    g = gcd(s, t)
    print(f"{s // g}/{t // g}")
else:
    print(s // t)