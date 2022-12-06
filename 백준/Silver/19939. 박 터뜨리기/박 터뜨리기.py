g = lambda: [*map(int, input().split())]

N, K = g()
N -= K * (K + 1) // 2
if N < 0:
    print(-1)
elif N % K:
    print(K)
else:
    print(K-1)