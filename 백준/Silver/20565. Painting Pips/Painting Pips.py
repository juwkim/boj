g = lambda: [*map(int, input().split())]

N, M = g()
r, q = divmod(M, N)
ans = 1
for _ in range(N-q):
    ans *= r / 6
for _ in range(q):
    ans *= (r+1) / 6
print(ans)