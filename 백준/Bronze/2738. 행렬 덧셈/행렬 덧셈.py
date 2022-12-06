g = lambda: [*map(int, input().split())]
N, M = g()
A = [g() for _ in range(N)]
for i in range(N):
    print(*[a + b for a, b in zip(A[i], g())])