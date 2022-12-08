g = lambda: [*map(int, input().split())]

from bisect import bisect
N = int(input())
A, B = g(), g()
for i in range(N):
    print(bisect(B, A[i]) - i - 1, end=' ')