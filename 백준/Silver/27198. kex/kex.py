g = lambda: [*map(int, input().split())]
n, q = g()
A = g()
s, e, skiped = 0, 0, 0
ans = [0] * q
for i, k in sorted(enumerate(g()), key=lambda x: x[1]):
    d = k - 1 - skiped
    while e < n and d >= A[e] - s:
        add = A[e] - s
        skiped += add
        d -= add
        s = A[e] + 1
        e += 1
    ans[i] = s + d
print(*ans)