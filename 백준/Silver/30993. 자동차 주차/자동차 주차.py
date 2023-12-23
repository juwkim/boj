import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from math import factorial as f

N, A, B, C = g()
ans = f(N) // (f(A) * f(B) * f(C))
print(ans)