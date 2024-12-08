import sys
g = lambda: map(int, sys.stdin.readline().split())

N, K = g()
P, *A = g()
Q, *B = g()
for a, b in zip(A, B):
    P, Q = min(P + a, Q + K + a), min(Q + b, P + K + b)
print(min(P, Q))