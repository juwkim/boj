import sys
g = lambda: map(int, sys.stdin.readline().split())

ans = 0
N, S, E = g()
for _ in range(N):
    R, A, D = g()
    q1, r1 = divmod(S, R + A)
    q2, r2 = divmod(E, R + A)
    if q1 == q2:
        ans += D / A * (max(r2, R) - max(r1, R))
    else:
        ans += D / A * (A - max(0, r1 - R))
        ans += D / A * max(0, r2 - R)
        ans += D * (q2 - q1 - 1)

print(ans / (E - S))