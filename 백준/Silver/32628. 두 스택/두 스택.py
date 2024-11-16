import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, K = g()
P = sum(A:= g())
Q = sum(B:= g())
for _ in range(K):
    if P > Q:
        P -= A.pop()
    else:
        Q -= B.pop()
print(max(P, Q))