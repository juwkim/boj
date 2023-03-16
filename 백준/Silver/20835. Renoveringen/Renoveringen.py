g = lambda: map(int, input().split())

from bisect import bisect_left

N, M = g()
A = sorted(g())
for num in g():
    idx = bisect_left(A, num)
    if idx == len(A) or A[idx] > num:
        if idx:
            del A[idx - 1]
    else:
        del A[idx]
print(len(A))
print(*A)