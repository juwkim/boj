import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import combinations

N, M = map(int, input().split())
A = [input() for _ in range(N)]
ones = [(i, j) for i in range(N) for j in range(M) if A[i][j] == '1']
zeros = [(i, j) for i in range(N) for j in range(M) if A[i][j] == '0']
print(min(max(min(abs(i - i1) + abs(j - j1), abs(i - i2) + abs(j - j2)) for i, j in ones) for (i1, j1), (i2, j2) in combinations(zeros, 2)))