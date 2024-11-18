import sys
g = lambda: map(int, sys.stdin.readline().split())

ans = 0
N, S, E = g()
for _ in range(N):
    R, A, D = g()
    q1, r1 = divmod(S, R + A)
    q2, r2 = divmod(E, R + A)
    ans += D * (q2 - q1) + D / A * (max(0, r2 - R) - max(0, r1 - R))
print(ans / (E - S))