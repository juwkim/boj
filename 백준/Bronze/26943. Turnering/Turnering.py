n, r = map(int, input().split())

A = list(range(1, 1 + n // 2))
B = list(range(n - 1, n // 2, -1))
for _ in range(r - 1):
    A, B = [B[0], *A[:-1]], [*B[1:], A[-1]]
B = [n, *B]

for a, b in zip(A, B):
    print(f'{a}-{b}')