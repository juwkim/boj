import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, L, W, H = g()
lo, hi = 0, min(L, W, H) + 1e-7
for i in range(1000):
    mid = (lo + hi) / 2
    if (L // mid) * (W // mid) * (H // mid) >= N:
        lo = mid
    else:
        hi = mid
print(lo)