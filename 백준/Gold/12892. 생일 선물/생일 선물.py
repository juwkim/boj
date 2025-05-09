import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, D = g()
P, V = zip(*sorted(g() for _ in range(N)))
ans, cur = V[0], V[0]
l, r = 0, 1
while r < N:
    if P[r] - P[l] < D:
        cur += V[r]
        ans = max(ans, cur)
        r += 1
    else:
        cur -= V[l]
        l += 1
print(ans)