from math import isqrt

for _ in range(int(input())):
    N = int(input())
    print((isqrt(2 * N * (N + 1) + 2) + 1) // 2)