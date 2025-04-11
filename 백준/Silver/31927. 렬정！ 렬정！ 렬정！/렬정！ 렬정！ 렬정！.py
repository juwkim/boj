N, *A = map(int, open(0).read().split())
print(N >> 1)
x = 1000000
for i in range(N >> 1):
    A[i] += x
    A[- 1 - i] -= x
    print(*A)
    x = min(1000000, A[i] - A[i+1], A[- 2 - i] - A[- 1 - i])