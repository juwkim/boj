g = lambda: [*map(int, input().split())]

n, p = g()
nums = [g() for _ in range(n)]
lo, hi = 0, 10**12
while hi > lo + 1:
    x = lo + hi >> 1
    cnt = 0
    for z, a, b in nums:
        if x < z:
            cnt += a * x
        else:
            cnt += a * z + b * (x - z)
    if cnt < p:
        lo = x
    else:
        hi = x
print(hi)