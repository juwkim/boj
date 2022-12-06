def solve(left):
    if not left:
        return 0
    Min = min(left)
    ret = 1000
    for step in range(1, max(Min + 1, m - Min) + 1):
        sub = set(range(Min - step * (Min // step), m, step))
        if sub.issubset(Set):
            ret = min(ret, solve(left - sub))
    return 1 + ret
while True:
    try:
        m, n, *nums = map(int, input().split())
        Set = set(nums)
        print(solve(Set))
    except:
        break