g = lambda: map(int, input().split()) 
N, M = g()
A = [[*g()] for _ in range(N)]
M, K = g()
B = [*zip(*[[*g()] for _ in range(M)])]
for i in range(N):
    print(*[sum(a * b for a, b in zip(A[i], B[j])) for j in range(K)], sep=" ")