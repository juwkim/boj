def solve():
    nums = [*map(int, input().split())]
    t = nums[0] + nums[1] + nums[4]
    if t & 1:
        return "NO"
    t >>= 1
    a, b, c = t - nums[4], t - nums[1], t - nums[0]
    d, e = nums[2] - a, nums[3] - a
    if a < 0 or b < 0 or c < 0 or d < 0 or e < 0:
        return "NO"
    if nums[5] != b + d or nums[6] != b + e:
        return "NO"
    if nums[7] != c + d or nums[8] != c + e:
        return "NO"
    if nums[9] != d + e:
        return "NO"
    return "YES"
print(solve())