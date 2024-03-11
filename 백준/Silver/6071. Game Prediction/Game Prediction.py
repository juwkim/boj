b = [*map(int, open(0).read().split())]
i = 0
tc = 1
while True:
    m, n = b[i], b[i + 1]
    i += 2
    if m == 0:
        break
    nums = sorted(b[i:i+n], reverse=True)
    i += n
    left = sorted(set(range(1, m * n + 1)) - set(nums), reverse=True)
    l, r = 0, len(left) - 1
    for num in nums:
        if left[l] > num:
            l += 1
    print(f"Case {tc}: {n - l}")
    tc += 1