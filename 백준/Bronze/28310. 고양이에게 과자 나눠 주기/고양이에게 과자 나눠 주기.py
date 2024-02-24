import sys
input = sys.stdin.readline
from fractions import Fraction
g = lambda: map(int, input().split())

for _ in range(int(input())):
    N, M = g()
    cnt = [Fraction(0, 1) for _ in range(N)]
    for _ in range(M):
        V, *A = g()
        for i, num in enumerate(A):
            cnt[i] += Fraction(num, V)
    print(max(cnt) - min(cnt))