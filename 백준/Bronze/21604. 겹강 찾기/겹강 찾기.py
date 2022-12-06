g = lambda: [*map(int, input().split())]

N, M = g()
nums = [g() for _ in range(M)]
print(M)
for i in range(M):
    res = [nums[(i+k) % M][k % N] for k in range(N)]
    print(*res)