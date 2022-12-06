from math import comb
n, m = map(int, input().split())
print(comb(n-1, m-1))