N, *A = map(int, open(0).read().split())
A.sort()
a, b, c, d = A[0], A[1], A[-1], A[-2]
print(sum(A) + max(0, 2 * a * b - a - b, 2 * c * d - c - d))