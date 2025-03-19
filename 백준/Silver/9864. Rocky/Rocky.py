import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

tc = 1
dc, dr = (1, 0, -1, 0), (0, -1, 0, 1)
while (l:=g()) != [0, 0, 0]:
    n, m, r = l
    a = [[0] * (n + 1) for _ in range(m + 1)]
    while r:
        nums = g()
        r -= len(nums) >> 1
        for i in range(0, len(nums), 2):
            a[nums[i + 1]][nums[i]] = 1
    c, r = g()
    cnt, good = 0, True
    if c == 1: d = 0
    elif r == 1: d = 3
    elif c == n: d = 2
    else: d = 1
    while good:
        cnt += 1
        for num in (d, (d + 1) % 4, (d + 3) % 4, (d + 2) % 4):
            nc, nr = c + dc[num], r + dr[num]
            if not (1 <= nc <= n and 1 <= nr <= m):
                good = False
                break
            if a[nr][nc] == 0:
                c, r, d = nc, nr, num
                break
    print(f"Case {tc}: {c} {r} {cnt}")
    tc += 1