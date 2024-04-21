while True:
    N, *nums = map(int, input().split())
    if N == 0:
        break
    i = 2
    while i <= N:
        tmp = []
        l, r = 0, i >> 1
        for _ in range(i // 2):
            tmp.append((nums[l] + nums[r]) // 2)
            tmp.append((nums[l] - nums[r]) // 2)
            l += 1
            r += 1
        nums[:i] = tmp
        i <<= 1
    print(*nums)