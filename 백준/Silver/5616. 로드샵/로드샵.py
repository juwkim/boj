import math
n, m, r = map(int, input().split())
print(math.comb(n + r - n * m - 1, n - 1))