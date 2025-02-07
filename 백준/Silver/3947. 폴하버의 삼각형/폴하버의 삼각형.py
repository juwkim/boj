import sys
input = sys.stdin.readline
from fractions import Fraction

d = [[Fraction() for _ in range(402)] for _ in range(401)]
for k in range(401, 0, -1):
    d[401 - k][1] = 1 - sum(d[401 - k])
    for i in range(402 - k, 401):
        j = i + k - 400
        d[i][j] = d[i - 1][j - 1] * i / j

for _ in range(int(input())):
    m, k = map(int, input().split())
    print(d[m][k])