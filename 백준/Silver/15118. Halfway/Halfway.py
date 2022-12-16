from math import isqrt
N = int(input())
ans = (2 * N - isqrt(2 * N * N - 2 * N + [1, 3][N % 4 > 1])) // 2
print(ans)