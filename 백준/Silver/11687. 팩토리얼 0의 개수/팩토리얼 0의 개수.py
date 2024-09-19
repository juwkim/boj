N = int(input())
lo, hi = 1, 80_000_004
def solve(num):
    cnt = 0
    while num:
        cnt += (num := num // 5)
    return cnt
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if solve(mid * 5) > N:
        hi = mid
    else:
        lo = mid
print(lo * 5 if solve(lo * 5) == N else -1)