import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
from math import inf

for tc in range(1, 1 + int(input())):
    D, N = g()
    w = [1]
    for num in reversed(g()):
        w.append(w[-1] * num)
    w.reverse()
    Min, Max = inf, -inf
    for _ in range(N):
        val = sum(a * b for a, b in zip(w, g()))
        Min, Max = min(Min, val), max(Max, val)
    print(f"Data Set {tc}:\n{Max - Min}\n")