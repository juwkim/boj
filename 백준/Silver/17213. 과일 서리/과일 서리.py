from math import comb

N, M = map(int, open(0))
print(comb(M - 1, N - 1))