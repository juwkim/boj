import sys
input = sys.stdin.readline

S, C = map(int, input().split())
L = [int(input()) for _ in range(S)]
lo, hi = 1, max(L) + 1
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if sum(x // mid for x in L) >= C:
        lo = mid
    else:
        hi = mid
print(sum(L) - lo * C)