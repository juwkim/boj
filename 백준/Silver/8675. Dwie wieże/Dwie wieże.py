g = lambda: [*map(int, input().split())]

from bisect import bisect_left
n, m = g()
A, B = [0] + g(), [0] + g()
for i in range(1, n + 1):
    A[i] += A[i-1]
for i in range(1, m + 1):
    B[i] += B[i-1]
for i in range(n, -1, -1):
    idx = bisect_left(B, A[i])
    if idx == m + 1:
        continue
    if B[idx] == A[i]:
        ans = n + m - (idx + i)
        print(ans)
        break