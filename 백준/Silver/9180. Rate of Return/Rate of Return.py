l, idx, tc = open(0).read().split(), 0, 1
while (N:=int(l[idx])) != -1:
    m, t = int(l[idx + N * 2 + 1]) + 1, float(l[idx + N * 2 + 2])
    nums = [(m - int(l[i]), float(l[i + 1])) for i in range(idx + 1, idx + N * 2 + 1, 2)]
    lo, hi = 0, 1
    for i in range(100):
        mid = (lo + hi) / 2
        if sum(c * (1 + mid) ** d for d, c in nums) < t:
            lo = mid
        else:
            hi = mid
    print(f"Case {tc}: {lo:.5f}\n")
    idx += N * 2 + 3
    tc += 1