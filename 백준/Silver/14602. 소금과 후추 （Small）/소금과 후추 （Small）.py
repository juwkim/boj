g = lambda: [*map(int, input().split())]

M, N, K, W = g()
A = [g() for _ in range(M)]
for i in range(M - W + 1):
    for j in range(N - W + 1):
        nums = []
        for k in range(i, i + W):
            nums.extend(A[k][j:j+W])
        print(sorted(nums)[W*W>>1], end=' ')
    print()