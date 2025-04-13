from math import gcd

N, M = map(int, input().split())
g = gcd(N, M)
print(f"{N//g}/{M//g}")