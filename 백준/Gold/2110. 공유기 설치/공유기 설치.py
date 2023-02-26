input = __import__('sys').stdin.readline

N, C = map(int, input().split())
home = sorted(int(input()) for _ in range(N))

def check(mid, C):
    cnt, prev = 1, 0
    for i in range(1, N):
        if home[i] - home[prev] >= mid:
            prev = i
            cnt += 1
    return cnt >= C

lo, hi = 1, (home[-1] - home[0]) // (C - 1) + 1
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if check(mid, C): lo = mid
    else: hi = mid
print(lo)