def solve():
    N, *nums = map(int, open(0).read().split())
    if nums[0] > 0:
        return -1
    nums[0] = 0
    m, M, idx = 1, 1, 0
    for i in range(1, N):
        if nums[i] == -1:
            continue
        if nums[i] > nums[idx] + i - idx:
            return -1
        if nums[i] != nums[idx] + i - idx:
            m += 1
            M += i - idx - nums[i]
        idx = i
    M += N - 1 - idx
    return f"{m} {M}"

print(solve())