import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

n = int(input())
a, b = g(), g()
lo, hi = -1, max(max(a), max(b))
def solve(arr, w):
    prv = None
    for num in arr:
        if num <= w:
            continue
        if prv is None:
            prv = num
        elif prv == num:
            prv = None
        else:
            return False
    return prv is None

while hi > lo + 1:
    mid = lo + hi >> 1
    if solve(a, mid) and solve(b, mid):
        hi = mid
    else:
        lo = mid
print(hi)