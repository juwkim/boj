g = lambda: [*map(int, input().split())]
N, K = g()
A = g()
ans = 1e10
for s in range(1, 1001):
    num = sum(s + i * K != A[i] for i in range(N))
    ans = min(ans, num)
print(ans)